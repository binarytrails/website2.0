import os
from django.shortcuts import HttpResponse, render_to_response
from .models import User, Skill, Photo
from kedfilms import utils

IMG_DIR = "frontend/static/frontend/img/"

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

    last_edited = utils.getMostFileRecursively(
        "frontend/templates/frontend/articles/",
        ".html"
    )
    # drops 'frontend/templates/'
    last_edited = last_edited[last_edited.rfind('frontend'):]

    return render_to_response(
        last_edited, {
            "title": "Articles",
            "subtitle": "Subtitle"
        }
    )

# categories: ((GN,General), (PF,Portfolio))
def photos(request):

    if os.path.exists(IMG_DIR):
        return render_to_response(
            "frontend/sections/photos.html",{
                "title": "Photos",
                "subtitle": "Take a closer look...",
                "portfolio_title": "Porfolio",
                "portfolio_images": Photo.objects.all().filter(category = Photo.PF),
                "general_title": "General",
                "general_images": Photo.objects.all().filter(category = Photo.GN)
        }
    )
