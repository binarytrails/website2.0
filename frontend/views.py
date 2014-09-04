# Controllers -> Views ("/templates/")

import os
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from kedfilms import utils

static_path = "frontend/static/frontend/"
images_dir = static_path + "img/"

def home(request):
	return render_to_response("frontend/home.html", {"title" : "Kpowwaaa!!!"})

def photos(request):

	if os.path.exists(images_dir):
		images = utils.get_filenames(images_dir, True)
		return render_to_response("frontend/photos.html", {"images": images, "title": "Photos"})
