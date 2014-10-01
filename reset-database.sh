#!/bin/bash

source scripts/bash/generic/makechoice
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
./manage.py shell < scripts/database/photos.py
echo; echo "Everything is done! Launching the server..."; echo
./manage.py runserver
