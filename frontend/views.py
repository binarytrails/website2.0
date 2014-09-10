# Controllers -> Views ("/templates/")

import os
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from kedfilms import utils
from .models import Photo, Skill

staticPath = "frontend/static/frontend/"
imagesDir = staticPath + "img/photos/"

def home(request):
	# CS: Computer Science
	cs_subcats = {}
	filterargs = {
      'category': 'CS',
      'owner': 'VI'
   }
	for skill in Skill.objects.all().filter(**filterargs).distinct():
		cs_subcats[str(skill.subcategory)] = skill.get_subcategory_display()

	return render_to_response(
   "frontend/home.html",{
		"title" : "Home",
		"subtitle": "Subtitle",
		"cs_subcats": cs_subcats,
		"skills": Skill.objects.all().filter(**filterargs)
	})

def photos(request):
	if os.path.exists(imagesDir):
		return render_to_response(
         "frontend/photos.html",{
		      "title": "Photos",
            "subtitle": "Subtitle",
            "photos": Photo.objects.all()
      })

