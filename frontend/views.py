# Controllers -> Views ("/templates/")

import os
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from kedfilms import utils
from .models import Photo

staticPath = "frontend/static/frontend/"
imagesDir = staticPath + "img/photos/"

def home(request):
	return render_to_response("frontend/home.html", {"title" : "Kpowwaaa!!!"})

def photos(request):
	if os.path.exists(imagesDir):
		#images = utils.getFilenames(imagesDir, True)
		return render_to_response("frontend/photos.html", {"title": "Photos", "subtitle": "Subtitle", "photos": Photo.objects.all()})

def blog(request):
	return render_to_response("frontend/blog.html")
