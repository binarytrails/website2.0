#!/bin/bash
rm -r frontend/migrations/
rm kedfilms/kedfilms.sqlite3
echo
echo "Creating database with South wrapper"
echo
./manage.py schemamigration frontend --initial
./manage.py syncdb
./manage.py migrate frontend
./manage.py shell < shellscripts/database/users.py
./manage.py shell < shellscripts/database/sections.py
./manage.py shell < shellscripts/database/skills.py
./manage.py shell < shellscripts/database/photos.py
echo 
echo "Everything is done! Launching the server..."
echo
./manage.py runserver
