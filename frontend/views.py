# Copyright (C) 2016 Seva Ivanov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either platform 3 of the License, or
# (at your option) any later platform.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os, random

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from .models import Category, Photo, Video, Project

from kedfilms import utils
from kedfilms.settings import MOBILE_HOSTS

APP = "frontend"
THEME = os.path.join(APP, "themes/bits")
ERRORS = os.path.join(APP, "themes/generic")
HEAD_TITLES = ["e a I a o", "The one and only",
    "I'm not the one", "________"]

MEDIA = settings.MEDIA_URL
STATIC = os.path.join(settings.STATIC_ROOT, APP)
APP_ROOT = os.path.abspath(os.path.dirname(__file__))

def is_mobile(request):
    # .mobile -> minidetector.Middleware
    return request.mobile or request.get_host() in MOBILE_HOSTS

def template_exists(template):
    return os.path.exists(os.path.join(APP_ROOT, "templates", template))

def template_prefix(request):
    return ("-mobile.html" if is_mobile(request) else ".html")

def merge_context(request, new_context=None):
    base_context = {
        "APP": APP,
        "THEME": THEME,
        "HEAD_TITLE": HEAD_TITLES[random.randint(0, 3)],
        "PLATFORM": "mobile" if is_mobile(request) else "desktop",
        "PARENT": os.path.join(THEME, "base" + template_prefix(request))
    }
    if new_context:
        return utils.merge_dicts(base_context, new_context)
    return base_context

# decorators

IE_USERAGENT_TAGS = ["msie", "trident"]

def old_browsers(initial_view):

    def wrapped_view(request, *args, **kwargs):
        ie_useragent = any(agent in request.META["HTTP_USER_AGENT"].lower() 
            for agent in IE_USERAGENT_TAGS)

        if ie_useragent:
            template = os.path.join(ERRORS, "old-browser.html")
            if template_exists(template) == False: return error404(request)

            return render(request, template, merge_context(request, {     
                "PARENT": os.path.join(ERRORS, "base.html"),
                "THEME": ERRORS,
                "SUPPORTED_BROWSERS": {"Firefox" ,"Chrome", "Safari"}
            }))

        return initial_view(request, *args, **kwargs)

    return wrapped_view

# views

@never_cache
@old_browsers
def home(request):
    template = os.path.join(THEME, "home.html")
    if template_exists(template) == False: return error404(request)
    
    return render(request, template, merge_context(request))

@never_cache
@old_browsers
def articles(request):
    template = os.path.join(THEME, "articles.html")
    if template_exists(template) == False: return error404(request)
    
    return render(request, template, merge_context(request))

@never_cache
@old_browsers
def article(request, category=None, article=None):
    if not article or not category: return error404(request)

    article_path = os.path.join(STATIC, "md/", category, article + ".md")
    if os.path.isfile(article_path) == False: return error404(request)

    template = os.path.join(THEME, "article.html")
    if template_exists(template) == False: return error404(request)
    
    return render(request, template, merge_context(request, {
        "html": utils.markdownToHtml(os.path.join(article_path))
    }))

@never_cache
@old_browsers
def projects(request):
    template = os.path.join(THEME, "projects.html")
    if template_exists(template) == False: return error404(request)

    return render(request, template, merge_context(request, {
        "start_year": 2015,
        "passed_years": range(3),
        "months": range(12, 0, -1),
        "projects": Project.TIMELINE
    }))

@never_cache
@old_browsers
def photos(request):
    template = os.path.join(THEME, "photos" + template_prefix(request))
    if not template_exists(template):
        return error404(request)

    return render(request, template, merge_context(request, {
        "categories": Category.objects.all().filter(context = "Photo")
    }))

@never_cache
@old_browsers
def gallery(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return error404(request)

    context = merge_context(request, {
        "category": category,
        "photos": Photo.objects.all().filter(
            category = category_id).order_by("-date_created")
    })

    if not is_mobile(request):
        last = next = -1
        categories = Category.objects.filter(context="Photo")
        for index in range(len(categories)):
            if categories[index].id == int(category_id):
                last = (index - 1) % (len(categories))
                next = (index + 1) % (len(categories))
                break
        context = utils.merge_dicts(context, {
            "last": categories[last].id,
            "next": categories[next].id
        })

    template = os.path.join(THEME, "photos-gallery" + template_prefix(request))
    if not template_exists(template):
        return error404(request)

    return render(request, template, context)

@never_cache
@old_browsers
def slideshow(request, category_id, fragment_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return error404(request)

    context = None
    if is_mobile(request):
        image = Photo.objects.get(fragment_identifier = fragment_id)
        if not os.path.isfile(image.get_image_abspath()):
            return error404(request)
        context = {"image_url": image.get_image_url()}
    else:
        context = {
            "category": category,
            "photos": Photo.objects.all().filter(
                category = category_id).order_by("-date_created")
        }

    template = os.path.join(THEME, "photos-slideshow" + template_prefix(request))
    if template_exists(template) == False: return error404(request)

    return render(request, template, merge_context(request, context)) 

@never_cache
@old_browsers
def videos(request):
    template = os.path.join(THEME, "videos" + template_prefix(request))
    if template_exists(template) == False: return error404(request)

    return render(request, template, merge_context(request, {
        "posters_url": os.path.join(STATIC, "img/video-poster/"),
        "videos_url": os.path.join(STATIC, "vid/"),
        "categories": Video.CATEGORIES,
        "videos": Video.objects.all().filter().order_by("-date_created")
    }))

# errors

def error404(request):
    template = os.path.join(ERRORS, "simple-text.html")
    if template_exists(template) == False: return HttpResponse("404 Not Found")

    return render(request, template, merge_context(request, {
        "PARENT": os.path.join(ERRORS, "base.html"),
        "THEME": ERRORS,
        "header": "404 NOT FOUND",
        "subtitle": """
            Sorry, the page you requested was not found.
        """
    }))

def no_mobile(request):
    template = os.path.join(ERRORS, "simple-text.html")
    if template_exists(template) == False: return error404(request)

    return render(request, template, merge_context(request, {
        "PARENT": os.path.join(ERRORS, "base.html"),
        "THEME": ERRORS,
        "header": "The mobile platform is not available.",
        "body": """
            Don"t worry, there is an easy fix.
            All you have to do is to consult our website using 
            your favorite computer to enjoy the experience to its fullest.
        """
    }))

def fullscreen_image(request, image_source):
    template = os.path.join(ERRORS, "fullscreen-image.html")
    if template_exists(template) == False: return error404(request)

    return render(request, template, merge_context(request, {
        "PARENT": os.path.join(ERRORS, "base.html"),
        "THEME": ERRORS,
        "image_source": image_source
    }))
