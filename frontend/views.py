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

import os, time

from django.shortcuts import HttpResponse, render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache

from .models import Photo, Video, Project
from kedfilms import utils
from projects import views_addons
import json

from django.conf import settings

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
STATIC_ROOT = settings.STATIC_ROOT
MEDIA_URL = settings.MEDIA_URL

STATIC_PROJECTS = os.path.join(STATIC_ROOT, "projects")
STATIC_FRONTEND = os.path.join(STATIC_ROOT, "frontend")
MEDIA_IMAGES = os.path.join(settings.MEDIA_ROOT, "images")

MOBILE_HOSTS = ["m.kedfilms.com", "m.sevaivanov.com"]
IE_USERAGENT_TAGS = ["msie", "trident"]

BASE_TEMPLATE = "base.html"

def error404(request):
    return render(request, "frontend/errors/generic-simple-text.html",
    {
        "header": "404 NOT FOUND",
        "subtitle": """
            Sorry, the page you requested was not found.
        """
    })

def is_mobile(request): return request.mobile or request.get_host() in MOBILE_HOSTS

def is_safari(request):
    user_agent = request.META["HTTP_USER_AGENT"].lower()
    return ("safari" in user_agent and "chrome" not in user_agent)

def get_app_version(request):
    if is_mobile(request): return "mobile"
    else: return "desktop"

def render_no_mobile_version(request):
    return render(request, "frontend/errors/generic-simple-text.html",
    {
        "header": "The mobile version is not available.",
        "body": """
            Don"t worry, there is an easy fix.
            All you have to do is to consult our website using 
            your favorite computer to enjoy the experience to its fullest.
        """
    })

def detect_old_browsers(initial_view):
    def wrapped_view(request, *args, **kwargs):
        if any(agent in request.META["HTTP_USER_AGENT"].lower() for agent in IE_USERAGENT_TAGS):
            browsers_suggestion = {"firefox": True, "chrome": True, "safari": True}
            return render(request, "frontend/errors/old-browser.html", browsers_suggestion)

        return initial_view(request, *args, **kwargs)
    return wrapped_view

@never_cache
@detect_old_browsers
def home(request):
    version = get_app_version(request)
    parent = os.path.join("frontend", version, BASE_TEMPLATE)

    return render(request, "frontend/generic/home.html", {
        "version": version,
        "parent": parent
    })

@never_cache
@detect_old_browsers
def projects(request):
    version = get_app_version(request)
    template = "frontend/generic/projects.html"
    parent = os.path.join("frontend", version, BASE_TEMPLATE)

    return render(request, template, {
        "parent": parent,
        "version": version,
        "start_year": 2015,
        "passed_years": range(3),
        "months": range(12, 0, -1),
        "projects": Project.TIMELINE
    })

@never_cache
@detect_old_browsers
def project(request, category, title, html_file):
    version = get_app_version(request)

    if version == "mobile": html_file += "-" + version
    html_file += ".html"
    
    template = os.path.join(category, title, html_file)
    template_abspath = os.path.join(PROJECT_ROOT, "projects/templates", template)

    if os.path.isfile(template_abspath) == False: return error404(request)

    # 3Dcube incompatibility with Safari
    if version == "desktop" and title == "home" and is_safari(request):
        browsers_suggestion = {"firefox": True, "chrome": True}
        return render(request, "frontend/errors/old-browser.html", browsers_suggestion)

    elif html_file == "mood-board.html":
        folder = os.path.join(STATIC_PROJECTS, "cart/moodboard/images/data")

        return render(request, template, {
            "version": version,
            "files": views_addons.moodboard(folder)
        })

    return render(request, template, {"version": version})

@never_cache
@detect_old_browsers
def articles(request):
    template = "frontend/generic/articles.html"
    parent = os.path.join("frontend", get_app_version(request), BASE_TEMPLATE)
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
    parent = os.path.join("frontend", get_app_version(request), BASE_TEMPLATE)
    html = utils.markdownToHtml(os.path.join(STATIC_FRONTEND, "md/", category, article))
 
    return render(request, template, { "parent": parent, "html": html })

@never_cache
@detect_old_browsers
def photos(request):
    categories = Photo.CATEGORIES
    
    if is_mobile(request):
        template = "frontend/mobile/photos.html"

        # omit the "internet in motion" aka the #4 section.
        # categories = [tuple(x for x in y if x)
        #     for y in categories if y != categories[4]
        # ]

    else:
        template = "frontend/desktop/photos.html"
    
    parent = os.path.join("frontend", get_app_version(request), BASE_TEMPLATE)

    return render(request, template,
    {
        "parent": parent,
        "categories": categories
    })

@never_cache
@detect_old_browsers
def gallery(request, category):
    if not os.path.exists(MEDIA_IMAGES): return Http404

    unique_categories = Photo.objects.all().values_list("category").distinct()
    if not unique_categories: return error404(request)

    if not any(unique_category[0] == category for unique_category in unique_categories):
        return error404(request)

    parent = os.path.join("frontend", get_app_version(request), BASE_TEMPLATE)

    if is_mobile(request):
        return render(request, "frontend/mobile/photos-gallery.html",
        {
            "parent": parent,
            "category": category,
            "photos": Photo.objects.all().filter(
                category = category).order_by("-date_created")
        })
    else:
        photo = Photo()
        return render(request, "frontend/desktop/photos-gallery.html",
        {
            "parent": parent,
            "category": category,
            "images": Photo.objects.all().filter(
                category = category).order_by("-date_created"),
            "last": photo.get_previous_category(category),
            "next": photo.get_next_category(category)
        })

@never_cache
@detect_old_browsers
def slideshow(request, category=None, fragment_id=None):
    if not any(unique_category["category"] == category
        for unique_category in Photo.objects.all().values("category").distinct()
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
                category = category).order_by("-date_created")
        })

@never_cache
@detect_old_browsers
def videos(request):
    parent = os.path.join("frontend", get_app_version(request), BASE_TEMPLATE)

    return render(request, "frontend/desktop/videos.html",
    {
        "parent": parent,
        "posters_src": "img/video-poster/",
        "videos_src": "vid/",
        "categories": Video.CATEGORIES,
        "videos": Video.objects.all().filter().order_by("-date_created")
    })
