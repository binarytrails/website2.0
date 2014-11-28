import os

from django.shortcuts import HttpResponse, render, redirect
from django.core.urlresolvers import reverse

from .models import User, Skill, Photo, Video
from kedfilms import utils
import json

DIR = os.path.abspath(os.path.dirname(__file__))
STATIC = "static/frontend"

IMG_DIR = os.path.join(DIR, STATIC, "img/")
VID_DIR = os.path.join(DIR, STATIC, "vid/")

ie_useragent_tags = ["msie", "trident"]

def detect_mobile(initial_view):
    def wrapped_view(request, *args, **kwargs):
        if request.mobile or "m.kedfilms.com" in request.get_host():
            calling_template = initial_view.func_name
            not_available_mobile_templates = ["articles", "photos", "videos"]

            if any(template in calling_template for template in not_available_mobile_templates):
                return render(request, "frontend/errors/generic-simple-text.html",
                {
                    "header": "Under Construction",
                    "image_src": "frontend/img/errors/beaver-ludge-with-leak.png",
                    "subtitle": """
                        The beavers are doing their best to build their lodge.
                    """,
                    "body": """
                        The mobile version of this page is under construction.
                        Don't worry, there is an easy fix!
                        Go on the desktop version which is fully functionnal.
                    """
                })

            return render(request, "frontend/errors/generic-simple-text.html",
            {
                "header": "The mobile version is not available.",
                "body": """
                    Don't worry, there is an easy fix.
                    All you have to do is to consult our website using 
                    your favorite computer to enjoy the experience to its fullest.
                """
            })
        # not mobile
        return initial_view(request, *args, **kwargs)

    # return what is returned from the wrapped_view()
    return wrapped_view

def get_home_args():
    skills_categories = []
    skills = Skill.objects.all().filter(owner='kedfilms-founder')

    for skill in skills.order_by('category').values('category').distinct():
        skills_categories.append(skill['category'])

    return {
        "skills_categories": skills_categories,
        "skills": Skill.objects.all().filter(owner='kedfilms-founder')
    }

def home(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        return redirect(reverse('mhome') + '#header')

    return render(request, "frontend/desktop/home.html", get_home_args())

def mhome(request):
    return render(request, "frontend/mobile/home.html", get_home_args())

def articles(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        template = "frontend/mobile/articles.html"
    else:
        template = "frontend/desktop/article.html"
 
    return render(request, template,
    {
        "html": utils.markdownToHtml(os.path.join(DIR, STATIC, "md/quick-tips/gpg.md"))
    })

def article(request, section=None, article=None):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        template = "frontend/mobile/article.html"
    else:
        template = "frontend/desktop/article.html"

    if article and section:
        article += ".md"
        if os.path.isfile(os.path.join(DIR, STATIC, "md/", section, article)) == False:
            raise Http404
        
        html = utils.markdownToHtml(os.path.join(DIR, STATIC, "md/", section, article))

        return render(request, template,
        {
            "html": html
        })

    raise Http404

def photos(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        categories = []
        for category in Photo.objects.all().values('category').distinct():
            categories.append(category['category'])

        return render(request, "frontend/mobile/photos.html",
        {
            'categories': categories,
            'photos': Photo.objects.all()
         })

    return redirect(reverse("frontend.views.gallery", kwargs={"section": "portfolio"}))

@detect_mobile
def gallery(request, section):
    if section and os.path.exists(IMG_DIR):
        if section == "portfolio":
            title = "Portfolio"
            category = Photo.PF
            thumbs_src = "img/portfolio/x200/"
            previous = "portfolio/#head"
            next = "general/#head"

        elif section == "general":
            title = "General"
            category = Photo.GN
            thumbs_src = "img/general/x200/"
            previous = "portfolio/#head"
            next = "general/#head"

        else:
            raise Http404

        return render(request, "frontend/desktop/gallery.html",
        {
            "section": section,
            "title": title,
            "images": Photo.objects.all().filter(
                category = category).order_by('-date_created'),
            "thumbs_src": thumbs_src,
            "previous": previous,
            "next": next
        })
    
    raise Http404

@detect_mobile
def slideshow(request, category=None):
    photos = None
    previous_location = "/photos/gallery/"

    if category == "portfolio":
        category_key = Photo.PF
        source = "img/portfolio/"
        previous_location += "portfolio/#head"

    elif category == "general":
        category_key = Photo.GN
        source = "img/general/"
        previous_location += "general/#head"

    else:
        raise Http404

    photos = Photo.objects.all().filter(
        category = category_key).order_by('-date_created')

    if photos:
        return render(request, "frontend/desktop/slideshow.html",
        {
            "photos": photos,
            "source": source,
            "category": category,
            "previous_location": previous_location,
        })
    
    raise Http404

@detect_mobile
def videos(request):
    if any(agent in request.META['HTTP_USER_AGENT'].lower() for agent in ie_useragent_tags):
        return render(request, "frontend/errors/old-browser.html")

    elif os.path.exists(VID_DIR):
        return render(request, "frontend/desktop/videos.html",
        {
            "posters_src": "img/video-poster/",

            "intro_title": "Brief introductory passage",
            "intro_videos": Video.objects.all().filter(
                category = Video.IN).order_by('-date_created'),
            "intro_videos_src": "vid/intro/",

            "favorite_title": "Personal Favorites",
            "favorite_videos": Video.objects.all().filter(
                category = Video.FV).order_by('-date_created'),
            "favorite_videos_src": "vid/favorite/",

            "event_title": "A Gathering Of People",
            "event_videos": Video.objects.all().filter(
                category = Video.EV).order_by('-date_created'),
            "event_videos_src": "vid/event/",

            "dancer_title": "Physical Expression",
            "dancer_videos": Video.objects.all().filter(
                category = Video.DN).order_by('-date_created'),
            "dancer_videos_src": "vid/dancer/"
        })
    
    raise Http404

def error404(request):
    return render(request, "frontend/errors/generic-bg-image.html",
    {
        "return_to": "/",
        "status": "404 NOT FOUND",
        "image_path": "frontend/img/gif/cats-night-ride.gif"
    })
