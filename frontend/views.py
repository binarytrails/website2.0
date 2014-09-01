# Controllers -> Views ("/templates/")

from django.shortcuts import render_to_response

def home(request):
	return render_to_response("frontend/home.html", {"hello" : "Hello world"})
