# Controllers -> Views ("/templates/")

import os
from django.shortcuts import HttpResponse, render_to_response
from kedfilms import utils
from .models import Photo, Skill

IMG_DIR = "frontend/static/frontend/img/"

def home(request):
	# CS: Computer Science
	cs_subcats = {}
	filterargs = {
      "category": "CS",
      "owner": "VI"
    }
	for skill in Skill.objects.all().filter(**filterargs).distinct():
		cs_subcats[str(skill.subcategory)] = skill.get_subcategory_display()

	return render_to_response(
        "frontend/home.html",{
		    "title" : "Home",
		    "subtitle": "Subtitle",
		    "cs_subcats": cs_subcats,
		    "skills": Skill.objects.all().filter(**filterargs)
	    }
    )

def articles(request):
    return render_to_response(
        "frontend/articles.html",{
            "title": "Articles",
            "subtitle": "Subtitle"
        }
    )

# categories: ((GN,General), (PF,Portfolio))
def photos(request):
    if os.path.exists(IMG_DIR):
        return render_to_response(
            "frontend/photos.html",{
                "title": "Photos",
                "subtitle": "Take a closer look...",
                "portfolioTitle": "Porfolio",
                "portfolioImages": Photo.objects.all().filter(category = "PF"),
                "generalTitle": "General",
                "generalImages": Photo.objects.all().filter(category = "GN")
        }
    )
