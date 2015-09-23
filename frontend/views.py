# Copyright (C) 2016 Seva Ivanov
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
from django.views.decorators.cache import never_cache

from .models import Skill, Photo, Video
from kedfilms import utils
import json

from django.conf import settings

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
STATIC_ROOT = settings.STATIC_ROOT
MEDIA_URL = settings.MEDIA_URL

STATIC_FRONTEND = os.path.join(STATIC_ROOT, "frontend")
MEDIA_IMAGES = os.path.join(settings.MEDIA_ROOT, "images")

MOBILE_HOSTS = ['m.kedfilms.com', 'm.sevaivanov.com']
IE_USERAGENT_TAGS = ["msie", "trident"]

def error404(request):
    return render(request, "frontend/errors/generic-simple-text.html",
    {
        "header": "404 NOT FOUND",
        "subtitle": """
            Sorry, the page you requested was not found.
        """
    })

def is_mobile(request): return request.mobile or request.get_host() in MOBILE_HOSTS

def get_app_version(request):
    if is_mobile(request): return "mobile"
    else: return "desktop"

def render_no_mobile_version(request):
    return render(request, "frontend/errors/generic-simple-text.html",
    {
        "header": "The mobile version is not available.",
        "body": """
            Don't worry, there is an easy fix.
            All you have to do is to consult our website using 
            your favorite computer to enjoy the experience to its fullest.
        """
    })

def detect_old_browsers(initial_view):
    def wrapped_view(request, *args, **kwargs):
        if any(agent in request.META['HTTP_USER_AGENT'].lower() for agent in IE_USERAGENT_TAGS):
            return render(request, "frontend/errors/old-browser.html")

        return initial_view(request, *args, **kwargs)
    return wrapped_view

def get_home_args():
    skills_categories = []
    skills = Skill.objects.all()

    for unique_category in skills.order_by('category').values('category').distinct():
        skills_categories.append(unique_category['category'])

    return {
        "skills_categories": skills_categories,
        "skills": Skill.objects.all()
    }

@never_cache
@detect_old_browsers
def home(request):
    if is_mobile(request):
        return render(request, "frontend/mobile/home.html", get_home_args())
    return render(request, "frontend/desktop/home.html", get_home_args())

@never_cache
@detect_old_browsers
def projects(request):
    if is_mobile(request): return render_no_mobile_version(request)
    
    template = "frontend/generic/projects.html"
    parent = os.path.join("frontend", get_app_version(request), "base.html")

    # Example; move to database.
    projects = {
        "2014-2":{
            "title": "The Koala",
            "description": "The koala is an arboreal herbivorous marsupial native to Australia. It is the only extant representative of the family Phascolarctidae, and its closest living relatives are the wombats.[3] The koala is found in coastal areas of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South Australia.",
            "preview-url": "/media/images/portfolio/x200/_MG_5499_final2.jpg"
        },
        "2012-4":{
            "title": "The Tiger",
            "description": "The tiger (Panthera tigris) is the largest cat species, reaching a total body length of up to 3.38 m (11.1 ft) over curves and exceptionally weighing up to 388.7 kg (857 lb) in the wild. Its most recognisable feature is a pattern of dark vertical stripes on reddish-orange fur with a lighter underside.",
            "preview-url": "/media/images/portfolio/x200/_MG_5499_final2.jpg"
        }
    }

    return render(request, template, {
        "parent": parent,
        "start_year": 2016,
        "passed_years": range(8),
        "months": range(12, 0, -1),
        "projects": projects
    })

@never_cache
@detect_old_browsers
def project(request, category, title, html_file):
    html_file += ".html"
    version = get_app_version(request)
    
    template = os.path.join(version, category, title, html_file)
    template_abspath = os.path.join(PROJECT_ROOT, "projects/templates", template)

    if os.path.isfile(template_abspath) == False: return error404(request)
    return render(request, template, {"version": version})

@never_cache
@detect_old_browsers
def articles(request):
    template = "frontend/generic/articles.html"
    parent = os.path.join("frontend", get_app_version(request), "base.html")
    return render(request, template, { "parent": parent })

@never_cache
@detect_old_browsers
def article(request, category=None, article=None):
    if not article or not category:
        return error404(request)

    article += ".md"
    if os.path.isfile(os.path.join(STATIC_FRONTEND, "md/", category, article)) == False:
        return error404(request)

    template = "frontend/generic/article.html"
    parent = os.path.join("frontend", get_app_version(request), "base.html")
    html = utils.markdownToHtml(os.path.join(STATIC_FRONTEND, "md/", category, article))
 
    return render(request, template, { "parent": parent, "html": html })

@never_cache
@detect_old_browsers
def photos(request):
    categories = Photo.CATEGORIES
    
    if is_mobile(request):
        template = "frontend/mobile/photos.html"

        # omit the 'internet in motion' aka the #4 section.
        categories = [tuple(x for x in y if x)
            for y in categories if y != categories[4]
        ]

    else:
        template = "frontend/desktop/photos.html"
    
    return render(request, template,
    {
        'categories': categories
    })

@never_cache
@detect_old_browsers
def gallery(request, category):
    if not os.path.exists(MEDIA_IMAGES): return Http404

    unique_categories = Photo.objects.all().values_list('category').distinct()
    if not unique_categories: return error404(request)

    if not any(unique_category[0] == category for unique_category in unique_categories):
        return error404(request)

    if is_mobile(request):
        return render(request, "frontend/mobile/photos-gallery.html",
        {
            "category": category,
            "photos": Photo.objects.all().filter(
                category = category).order_by('-date_created')
        })
    else:
        photo = Photo()
        return render(request, "frontend/desktop/photos-gallery.html",
        {
            "category": category,
            "images": Photo.objects.all().filter(
                category = category).order_by('-date_created'),
            "last": photo.get_previous_category(category),
            "next": photo.get_next_category(category)
        })

@never_cache
@detect_old_browsers
def slideshow(request, category=None, fragment_id=None):
    if not any(unique_category['category'] == category 
        for unique_category in Photo.objects.all().values('category').distinct()
    ):
        return error404(request)

    if is_mobile(request):
        image = Photo.objects.get(fragment_identifier = fragment_id)

        if os.path.isfile(image.get_image_abspath()) == False:
            return error404(request)

        return render(request, "frontend/mobile/photos-slideshow.html",
        {
            "image_url": image.get_image_url()
        })

    else:
        return render(request, "frontend/desktop/photos-slideshow.html",
        {
            "category": category,
            "photos": Photo.objects.all().filter(
                category = category).order_by('-date_created')
        })

@never_cache
@detect_old_browsers
def videos(request):
    return render(request, "frontend/desktop/videos.html",
    {
        "posters_src": "img/video-poster/",
        "videos_src": "vid/",
        "categories": Video.CATEGORIES,
        "videos": Video.objects.all().filter().order_by('-date_created')
    })

