# Copyright (C) 2014 Vsevolod Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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

    for unique_category in skills.order_by('category').values('category').distinct():
        skills_categories.append(unique_category['category'])

    return {
        "skills_categories": skills_categories,
        "skills": Skill.objects.all().filter(owner='kedfilms-founder')
    }

def entry(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        return redirect(reverse('home') + '#header')
    else:
        return render(request, "frontend/desktop/entry.html")

def home(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        return render(request, "frontend/mobile/home.html", get_home_args())

    return render(request, "frontend/desktop/home.html", get_home_args())

def articles(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        template = "frontend/mobile/articles.html"
        return render(request, template)
    else:
        template = "frontend/desktop/article.html"
 
        return render(request, template,
        {
            "html": utils.markdownToHtml(os.path.join(DIR, STATIC, "md/quick-tips/gpg.md"))
        })

def article(request, category=None, article=None):
    if not article or not category:
        raise Http404

    article += ".md"
    if os.path.isfile(os.path.join(DIR, STATIC, "md/", category, article)) == False:
        raise Http404

    html = utils.markdownToHtml(os.path.join(DIR, STATIC, "md/", category, article))

    if request.mobile or "m.kedfilms.com" in request.get_host():
        template = "frontend/mobile/article.html"
    else:
        template = "frontend/desktop/article.html"

    return render(request, template, { "html": html })

def photos(request):
    if request.mobile or "m.kedfilms.com" in request.get_host():
        categories = []
        for unique_category in Photo.objects.all().values('category').distinct():
            categories.append(unique_category['category'])

        return render(request, "frontend/mobile/photos.html",
        {
            'categories': categories,
            'photos': Photo.objects.all()
         })
    else:
        return redirect(reverse("frontend.views.gallery", kwargs={"category": "portfolio"}))

def gallery(request, category):
    if not os.path.exists(IMG_DIR):
        return Http404

    unique_categories = Photo.objects.all().values_list('category').distinct()

    if not unique_categories:
        raise Http404

    if not any(unique_category[0] == category for unique_category in unique_categories):
        raise Http404

    if request.mobile or "m.kedfilms.com" in request.get_host():
        return render(request, "frontend/mobile/photos-gallery.html",
        {
            "category": category,
            "photos": Photo.objects.all().filter(
                category = category).order_by('-date_created')
        })
    else:
        # {'category': {'last': 'category', 'previous': 'category'}, ... }1
        pages = utils.get_list_next_previous_as_two_dimentional_dict(unique_categories)

        return render(request, "frontend/desktop/photos-gallery.html",
        {
            "category": category,
            "images": Photo.objects.all().filter(
                category = category).order_by('-date_created'),
            "last": pages[category].get('last') + "/#head",
            "next": pages[category].get('next') + "/#head"
        })

@detect_mobile
def slideshow(request, category=None):
    if not any(unique_category['category'] == category 
        for unique_category in Photo.objects.all().values('category').distinct()
    ):
        raise Http404

    return render(request, "frontend/desktop/photos-slideshow.html",
    {
        "category": category,
        "photos": Photo.objects.all().filter(
            category = category).order_by('-date_created')
    })

def mslideshow(request, category=None, image=None):
    if not request.mobile and not "m.kedfilms.com" in request.get_host():
        return Http404

    path_to_image = os.path.join(STATIC, "img/", category, "original", image)
    abspath_to_image = os.path.join(DIR, path_to_image)

    if os.path.isfile(abspath_to_image) == False:
        raise Http404

    return render(request, "frontend/mobile/photos-slideshow.html",
    {
        "image_url": os.path.join("/", path_to_image)
    })

@detect_mobile
def videos(request):
    if any(agent in request.META['HTTP_USER_AGENT'].lower() for agent in ie_useragent_tags):
        return render(request, "frontend/errors/old-browser.html")

    if not os.path.exists(VID_DIR):
        raise Http404

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

def error404(request):
    return render(request, "frontend/errors/generic-simple-text.html",
    {
        "header": "404 NOT FOUND",
        "subtitle": """
            Sorry, the page you requested was not found.
        """
    })