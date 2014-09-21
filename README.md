# Kedfilms

Django html5 website

## Coding style
* Indent 4 spaces

## Plugin :  Description
* Linear : Base website template
* Swipebox : jQuery lightbox
* Django-debug-toolbar : Browser debug toolbar
* South : Database updater

## Database diagram : crow's foot notation

                                   +-----------+                        
                                   |    USER   |                                                              
                                   +-----------+                   
                               +-|<| NICK (PK1)|||-+                                                      
                               |   | NAME      |   |                    
                               |   | LASTNAME  |   |   +-----------------+
                               |   | EMAIL     |   |   |     PHOTO       |
                               |   +-----------+   |   |-----------------| 
    +----------------------+   |                   |   | FILENAME (PK1)  |
    |      ARTICLE         |   |                   |   | TITLE (U1)      |
    +----------------------+   |                   |   | DESCRIPTION     |
    | ID (PK1)             |   |                   |   | CATEGORY (U1)   |
    | TITLE (U1)           |   |                   |   | AUTHOR          |
    | SUBTITLE             |   |                   |   | DATE_CREATED    |
    | CATEGORY (U1)        |   |                   +-0<| OWNER (FK1,U1)  |
    | SUBCATEGORY (U1)     |   |                   |   +-----------------+
    | DATE_CREATED         |   |                   |
    | DATE_MODIFIED        |   |                   |   +------------------+
    | AUTHOR (FK1, U1)     |>0-+                   |   |     VIDEO        |
    +----------------------+                       |   +------------------+
     * set url manually                            |   | FILENAME (PK1)   |
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

### South

    ./manage.py schemamigration frontend --initial
    ./manage.py migrate frontend
    ./manage.py syncdb

    ./manage.py schemamigration frontend --auto
    ./manage.py migrate frontend

### Database population
   
    ./manage shell
    from frontend.models import Photo
    photo = Photo(title = "This is the world that you know.", 
    filename = "world_that_you_know-the_matrix.png", 
        description = "The Matrix (1999) by The Wachowski Brothers", 
        author = "The Wachowski Brothers")


