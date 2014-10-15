# Kedfilms
Avoiding scripts by implementing CSS stylish functionalities.

## Getting started

### 1. Create your virtual environment
Create a local virtual environment with all the tools inside

        virtualenv DJANGO

Activate virtualenv

        source DJANGO/bin/activate

Install django and its tools inside

        easy_install django==1.7 


### 2. Install ImageMagick
It is used for image resizing in the photos section. To complile it you would need some tools

        sudo apt-get install imagemagick

### Post-installation

Launch the website

        ./manage runserver

Remove installed dependencies
    
        easy_install -m [package]

Then you can remove locally left PackageName.egg

To quit the virtualenv

        deactivate


## Features

### Plugins
#### Active
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
	    | LASTNAME  |   |   +-----------------+
	    | EMAIL     |   |   |     PHOTO       |
	    +-----------+   |   |-----------------| 
	                    |   | FILENAME (PK1)  |
	                    |   | TITLE (U1)      |
	                    |   | DESCRIPTION     |
	                    |   | CATEGORY (U1)   |
	                    |   | AUTHOR          |
	                    |   | DATE_CREATED    |
	                    +-0<| OWNER (FK1,U1)  |
	                    |   +-----------------+
	                    |
	                    |   +------------------+
	                    |   |     VIDEO        |
	                    |   +------------------+
	                    |   | FILENAME (PK1)   |
	                    |   | TITLE (U1)       |
	                    |   | DESCRIPTION      |
	                    |   | CATEGORY (U1)    |
	                    |   | AUTHOR           |
	                    |   | DIRECTOR         |
	                    |   | SFX              |
	                    +-0<| OWNER (FK1,U1)   |
	                    |   +------------------+
	                    |
	                    |   +------------------+
	                    |   |     SKILL        |
	                    |   +------------------+
	                    |   | ID (PK1)         |
	                    |   | TITLE (U1)       |
	                    |   | DESCRIPTION      |
	                    |   | CATEGORY (U1)    |
	                    |   | SUBCATEGORY (U1) |
	                    |   | RATING_ON_FIVE   |
	                    +-0<| OWNER (FK1,U1)   |
	                        +------------------+
                                                                        
                             

## Tutorial

### Database script
    
        ./manage shell < script.py

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

