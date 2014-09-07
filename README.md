Kedfilms
========
Django html5 website


<table>
	<tr>
		<th><b>Plugin / Tool</b></th>
		<th><b>Description</b></th>
	</tr>
	<tr>
		<th>Linear</th>
		<th>Base website template</th>
	</tr>
	<tr>
		<th>Swipebox</th>
		<th>jQuery lightbox</th>
	</tr>
	<tr>
		<th>Django-debug-toolbar</th>
		<th>Browser debug toolbar</th>
	</tr>
	<tr>
		<th>South</th>
		<th>Database updater</th>
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

