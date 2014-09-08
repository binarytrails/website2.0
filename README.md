Kedfilms
========
Django html5 website


<table>
	<tr>
		<th><b>Plugin / Tool</b></th>
		<th><b>Description</b></th>
	</tr>
	<tr>
		<th>linear</th>
		<th>base website template</th>
	</tr>
	<tr>
		<th>swipebox</th>
		<th>jQuery lightbox</th>
	</tr>
	<tr>
		<th>django-debug-toolbar</th>
		<th>browser debug toolbar</th>
	</tr>
	<tr>
		<th>south</th>
		<th>database updater</th>
	</tr>
</table>
	

How to
------

<b>South</b>

	./manage.py schemamigration frontend --initial
	./manage.py migrate frontend
	./manage.py syncdb

	./manage.py schemamigration frontend --auto
	./manage.py migrate frontend

<b>Database population</b>
	
	./manage shell
	from frontend.models import Photo
	photo = Photo(title = "This is the world that you know.", 
			filename = "world_that_you_know-the_matrix.png", 
			description = "The Matrix (1999) by The Wachowski Brothers", 
			author = "The Wachowski Brothers")

