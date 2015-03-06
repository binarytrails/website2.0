# Kedfilms
Avoiding scripts by implementing CSS stylish functionalities.


## Dependecies

* Markdown2 : Convert articles markdown text -> Html
* ImageMagick : Thumbnails creation
* Pillow: Images handling
* pyexiv2: Images xmp metadata


## Getting started

Create a local virtual environment with all the tools inside

        virtualenv -p python2.7 DJANGO

Activate virtualenv

        source DJANGO/bin/activate

Install django and its dependecies

        easy_install django==1.7 markdown2==2.3.0 


## General

* Launch the website

        ./manage runserver

* Remove installed dependencies
    
        easy_install -m [package]

Then you can remove locally left PackageName.egg

* Create the database while drinking a coffee

        ./reset-database.sh

* Populate it by hand

        ./manage shell < script.py

* Quit the virtualenv

        deactivate

WARNING: If you move your project after creating your virtualenv it won't work anymore.

        vim DJANGO/bin/activate
        # find VIRTUAL_ENV='old/path/DJANGO' and change the old path


## Apache2 + mod_wsgi (testing only)

Run apache2 + mod_wsgi server on your local network to test it with mutiple devices. Apache2 is on Debian. It is very similar to the normal apache layout.

		apt-get install apache2 libapache2-mod-wsgi

Remove it from the start up levels

		apt-get install sysv-rc-conf && sysv-rc-conf

Add apache2 basic configuration

		vim /etc/apache2/sites-available/kedfilms-dev

[kedfilms-dev] file example using virtualenv

		NameVirtualHost *:999
		Listen 999
		WSGIPythonPath /path/to/django-kedfilms-project:/path/to/django-kedfilms-project/DJANGO/lib/python2.7/site-packages

		WSGIScriptAlias / /path/to/django-kedfilms-project/kedfilms/wsgi.py
		<Directory /path/to/django-kedfilms-project/kedfilms>
		<Files wsgi.py>
		    Allow from all
		</Files>
		</Directory>

		Alias /static/ /path/to/django-kedfilms-project/frontend/static/

		<Directory /path/to/django-kedfilms-project/frontend/static>
		    Allow from all
		</Directory>

Add a symbolic link which will allow apache to collect [kedfilms-dev] settings from [sites-available] folder.

		ln -s /etc/apache2/sites-available/kedfilms-dev
