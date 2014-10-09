import os
from django.shortcuts import HttpResponse, render_to_response
from .models import User, Skill, Photo
from kedfilms import utils

IMG_DIR = "frontend/static/frontend/img/"
VID_DIR = "frontend/static/frontend/vid/"

def home(request):

    skills_categories = []
    for item in Skill.objects.all().filter(owner='kedfilms-founder').order_by('category').values('category').distinct():
        skills_categories.append(item['category'])

    return render_to_response(
        "frontend/sections/home.html",{
            "skills_categories": skills_categories,
            "skills": Skill.objects.all().filter(owner='kedfilms-founder')
        }
    )

def articles(request):

    try:
        last_edited = utils.getMostRecentFileRecursively(
            "frontend/templates/frontend/articles/",
            ".html"
        )
        # drops 'frontend/templates/'
        template = last_edited[last_edited.rfind('frontend'):]

    except ValueError:
        template = "frontend/sections/articles.html"    

    return render_to_response(
        template, {
            "title": "Articles",
            "subtitle": "Subtitle"
        }
    )

# categories: ((GN,General), (PF,Portfolio))
def photos(request):

    if os.path.exists(IMG_DIR):
        return render_to_response(
            "frontend/sections/photos.html",{
                "title": "Photography",
                "subtitle": "Capture the moment in time",
                "portfolio_title": "Porfolio",
                "portfolio_images": Photo.objects.all().filter(category = Photo.PF),
                "general_title": "General",
                "general_images": Photo.objects.all().filter(category = Photo.GN)
        }
    )

# tmp: load from photos
def videos(request):

    if os.path.exists(VID_DIR):
        return render_to_response(
            "frontend/sections/videos.html",{
                "title": "Short Films",
                "intro_title": "Brief introductory passage",
                "intro_videos": "",
                "complete_title": "The affair is over, ended, finished",
                "complete_videos": "",
                "unofficial_title": "An incomplete flower",
                "unofficial_videos": ""
        }
    )

def slideshow(request, filestype=None, category=None):

    files = None

    if filestype == "photo":
        if category == "portfolio":
            category = Photo.PF

        elif category == "general":
            category = Photo.GN

        files = Photo.objects.all().filter(category = category)

    elif filestype == "video":
        if category == "intro":
            pass

        elif category == "complete":
            pass

        elif category == "unofficial":
            pass

        files = 1

    if files:
        return render_to_response(
            "frontend/sections/slideshow.html",{
                "filestype": filestype,
                "files": files
        })
