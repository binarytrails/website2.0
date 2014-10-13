#!/bin/bash

source scripts/bash/makechoice
makechoice "Do you accept the database and the migrations removal?"

if [ $run == false ]; then
    exit 0
fi

rm -r frontend/migrations/
rm kedfilms/kedfilms.sqlite3
mkdir frontend/migrations/
touch frontend/migrations/__init__.py

echo; echo "Creating database with South wrapper"; echo
./manage.py makemigrations
./manage.py syncdb
./manage.py migrate
./manage.py shell < scripts/database/users.py
./manage.py shell < scripts/database/skills.py

echo; echo "Should we create a moq for photos mapped in 'scripts/database/photos.py'? (yes, no):"; read moqphotos
if [ "$moqphotos" == "yes" ]; then
    ./manage.py shell < scripts/database/photos-moq.py
else
    ./manage.py shell < scripts/database/photos.py
fi

echo; echo "Do you have original videos mapped in 'scripts/database/videos.py'? (yes, no):"; read hasvideos
if [ "$hasvideos" == "yes" ]; then
    ./manage.py shell < scripts/database/videos.py
fi

echo; echo "Everything is done! Launching the server..."; echo
./manage.py runserver
