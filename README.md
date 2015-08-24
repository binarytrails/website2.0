# Kedfilms

*Avoiding scripts by implementing CSS stylish functionalities.*

This is my personal website using the Django Python Web framework that I built to centralize my realizations and gain web development experience. I challenged myself to only use CSS3 & HTML5 and leave JavaScript aside. I wanted to gain deep understanding of the trivial web technologies as well as demonstrate that JavaScript is not always necessary for a modern website.

*Why Kedfilms?* Once upon a time, I had to decide what brand name I would put my projects under and this name came out. I kept it considering that it is easier to remember and simpler than putting my complete name everywhere.

There are two different layouts of this website. The first is for the desktop experience and the second is for mobile users.

There is a detection of a mobile device, but if you're on a laptop browsing the desktop version and you're wishing to see the mobile version you can navigate to the *m* subdomain as in *m.kedfilms.com*.

This website is completely Open-Source under GPLv3 license. Although I encourage folks to inspire themselves from it, I would appreciate it if you do not copy completely its looks so that it stays a unique representation of my work in which I put numerous hours of mine.

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

* Populate database from script.py

        ./manage shell < script.py

* Quit the virtualenv

        deactivate

WARNING: If you move your project after creating your virtualenv it won't work anymore.

        vim DJANGO/bin/activate
        # find VIRTUAL_ENV='old/path/DJANGO' and change the old path

## Test it with mutiple devices 

When the server is listening on *0.0.0.0*, it is waiting for the requests on all available network interfaces. In other words, you're opening a port that can be accessed by external devices using your ip and the below port.

        ./manage runserver 0.0.0.0:8000

## Debian Basic Server: Apache2 + mod_wsgi

Apache2 is on Debian. It is very similar to the normal apache layout.

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
