# Controllers -> Views ("/templates/")

import os
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from kedfilms import utils

staticPath = "frontend/static/frontend/"
imagesDir = staticPath + "img/photos/"

def home(request):
	return render_to_response("frontend/home.html", {"title" : "Kpowwaaa!!!"})

def photos(request):

	if os.path.exists(imagesDir):
		images = utils.getFilenames(imagesDir, True)
		return render_to_response("frontend/photos.html", {"images": images, "title": "Photos"})
