# Kedfilms
Avoiding scripts by implementing CSS stylish functionalities.

## Getting started

### 1. Create your virtual environment
Create a local virtual environment with all the tools inside

        virtualenv DJANGO

Activate virtualenv

        source DJANGO/bin/activate

Install django and its tools inside

        easy_install django==1.7 markdown2==2.3.0 


### 2. Install ImageMagick
It is used for image resizing in the photos section. To complile it you would need some tools

        sudo apt-get install imagemagick

### Post-installation

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

## Features
### Plugins
#### Active
* Markdown2 : Markdown text to Html
* ImageMagick : Convert, Edit, and Compose Images

#### Recommended
* Django-debug-toolbar : Browser debug toolbar

		easy_install django_debug_toolbar

### Add-ons
* Reset CSS : Stylesheet to reduce browser inconsistencies
* Swipebox : jQuery lightbox


## Database diagram : crow's foot notation

* Articles works on behalf of a folder structure

		user/category/subcategory/article-base.html

* Database is used to store technical information used in templates

	    +-----------+
	    |    USER   |
	    +-----------+
	    | NICK (PK1)|||-+ 
	    | NAME      |   | 
	    | LASTNAME  |   |   +-------------------------+
	    | EMAIL     |   |   |          PHOTO          |
	    +-----------+   |   +-------------------------+
	                    |   | STATICFILEPATH (PK1)    |
	                    |   | FRAGMENT_IDENTIFIER (U1)|
	                    |   | TITLE (U2)              |
	                    |   | AUTHOR                  |
	                    |   | CATEGORY (U2)           |
	                    |   | HARDWARE                |
	                    |   | APPLICATION             |
	                    |   | DATE_CREATED            |
	                    |-0<| OWNER (FK1, U2)         |
	                    |   +-------------------------+
	                    |                        
	                    |   +-------------------------+
	                    |   |          VIDEO          |
	                    |   +-------------------------+    
	                    |   | STATICFILEPATH (PK1)    | 
	                    |   | STATICPOSTERPATH (U1)   |
	                    |   | TITLE (U2)              |
	                    |   | DIRECTOR                |
	                    |   | DESCRIPTION             |
	                    |   | CATEGORY (U2)           |
	                    |   | HARDWARE                |
	                    |   | APPLICATION             |
	                    |   | DATE_CREATED            |
	                    |-0<| OWNER (FK1, U2)         |
	                    |   +-------------------------+
	                    |                        
	                    |   +-------------------------+
	                    |   |          SKILL          |
	                    |   +-------------------------+
	                    |   | ID (PK1)                |
	                    |   | TITLE (U1)              |
	                    |   | DESCRIPTION             |
	                    |   | CATEGORY (U1)           |
                        |   | RATING_ON_FIVE          |
                        +-0<| OWNER (FK1, U1)         |
                            +-------------------------+                 
                             

## Coding style
* Indent 4 spaces

* Functions & variables

    * If you can read it, make it simple

            makechoice

    * Otherwise

            awesome_variable
    
    * Global static variables are uppercase

            AWESOME_STATIC_VARIABLE

* Priority to new line per bracket

        function
        {
            # code here
        }
        
* If not permitted, one new line for last bracket i.e. views.py

        function{
            # code here
        }

* Create database tables only if necessary

	    * To reduce code redundance
	    * To stock object related information

