Kedfilms
========
Django html5 website

templates
---------
linear

plugins
-------
swipebox

dev-tools
---------
django-debug-toolbar
south - db migrations
	

how to?
=======
south
-----
	./manage.py schemamigration frontend --initial
	./manage.py migrate frontend
	./manage.py syncdb

	./manage.py schemamigration frontend --auto
	./manage.py migrate frontend

database population
-------------------
./manage shell
from frontend.models import Photo
photo = Photo(title = "This is the world that you know.", 
		filename = "world_that_you_know-the_matrix.png", 
		description = "The Matrix (1999) by The Wachowski Brothers", 
		author = "The Wachowski Brothers")

