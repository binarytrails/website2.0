import os
from django.shortcuts import HttpResponse, render
from .models import User, Skill, Photo, Video
from kedfilms import utils

DIR = os.path.abspath(os.path.dirname(__file__))
STATIC = "static/frontend"

IMG_DIR = os.path.join(DIR, STATIC, "img/")
VID_DIR = os.path.join(DIR, STATIC, "vid/")

ie_useragent_tags = ["MSIE", "Trident"]

def detect_mobile(initial_view):
    def wrapped_view(request, *args, **kwargs):
        if request.mobile:
            return render(request, "frontend/errors/unsupported-mobile.html")

        return initial_view(request, *args, **kwargs)
    return wrapped_view

#@detect_mobile
def home(request):
    return render(request, "frontend/mobile/home.html")
    # # if request.mobile:
    # #     return render(request, "frontend/mobile/home.html")

    # skills_categories = []

    # for item in Skill.objects.all().filter(
    #     owner='kedfilms-founder'
    # ).order_by('category').values('category').distinct():

    #     skills_categories.append(item['category'])

    # return render(request, "frontend/desktop/home.html",
    # {
    #     "skills_categories": skills_categories,
    #     "skills": Skill.objects.all().filter(owner='kedfilms-founder')
    # })

@detect_mobile
def articles(request):
    return render(request, "frontend/desktop/article.html",
    {
        "html": utils.markdownToHtml(os.path.join(DIR, STATIC, "md/quick-tips/gpg.md"))
    })

@detect_mobile
def article(request, section=None, article=None):
    if article and section:
        article += ".md"
        if os.path.isfile(os.path.join(DIR, STATIC, "md/", section, article)) == False:
            raise Http404
        
        html = utils.markdownToHtml(os.path.join(DIR, STATIC, "md/", section, article))

        return render(request, "frontend/desktop/article.html",
        {
            "html": html
        })

    else:
        raise Http404

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
    else:
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

    photos = Photo.objects.all().filter(category = category_key)

    if photos:
        return render(request, "frontend/desktop/slideshow.html",
        {
            "photos": photos,
            "source": source,
            "category": category,
            "previous_location": previous_location,
        })
    else:
        raise Http404

@detect_mobile
def videos(request):
    if any(agent in request.META['HTTP_USER_AGENT'] for agent in ie_useragent_tags):
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
    else:
        raise Http404

def error404(request):
    return render(request, "frontend/errors/generic-bg-image.html",
    {
        "return_to": "/",
        "status": "404 NOT FOUND",
        "image_path": "frontend/img/gif/cats-night-ride.gif"
    })
