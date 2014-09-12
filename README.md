# Kedfilms

Django html5 website

## Coding style
* Indent 4 spaces

## Plugin :  Description
* Linear : Base website template</th>
* Swipebox : jQuery lightbox</th>
* Django-debug-toolbar : Browser debug toolbar</th>
* South : Database updater</th>

## Database diagram : crow's foot notation

                                +-----------+                        
                                |    USER   |                                         
                                +-----------+                        
                            +-|<| NICK (PK1)|||-+                           
                            |   | NAME      |   |                    
                            |   | LASTNAME  |   |                    
                            |   | EMAIL     |   |                     
                            |   +-----------+   |                       
    +-------------------+   |                   |   +-----------------+
    |      ARTICLE      |   |                   |   |      PHOTO      |
    +-------------------+   |                   |   +-----------------+
    | ID (PK1)          |   |                   |   | FILENAME (PK1)  |
    | TITLE (U1)        |   |                   |   | TITLE (U1)      |
    | SUBTITLE          |   |                   |   | DESCRIPTION     |
    | CATEGORY (U2)     |   |                   +-0<| OWNER (FK1,U1)  |
    | SUBCATEGORY (U2)  |   |                   |   +-----------------+
    | DATE_CREATED      |   |                   |
    | DATE_MODIFIED     |   |                   |   +------------------+
    | AUTHOR (FK1,U1,U2)|>0-+                   |   |     VIDEO        |
    +-------------------+                       |   +------------------+
     * set url manually                         |   | FILENAME (PK1)   |
                                                |   | TITLE (U1)       |
                                                |   | DESCRIPTION      |
                                                |   | CATEGORY (U2)    |
                                                |   | AUTHOR           |
                                                |   | DIRECTOR         |
                                                |   | SFX              |
                                                +-0<| OWNER (FK1,U1,U2)|
                                                |   +------------------+
                                                |
                                                |   +------------------+
                                                |   |     SKILL        |
                                                |   +------------------+
                                                |   | ID (PK1)         |
                                                |   | TITLE (U1)       |
                                                |   | CATEGORY (U2)    |
                                                |   | SUBCATEGORY (U2) |
                                                |   | DESCRIPTION      |
                                                |   | RATING_ON_FIVE   |
                                                +-0<| OWNER (FK1,U1,U2)|
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


