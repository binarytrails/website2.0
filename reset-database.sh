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
./manage.py shell < scripts/database/videos.py

echo; echo "Do you have the original photos (not in github)? (yes, no):"; read hasphotos
if [ "$hasphotos" == "no" ]; then
    ./manage.py shell < scripts/database/photos-moq.py
else
    ./manage.py shell < scripts/database/photos-porfolio.py
    ./manage.py shell < scripts/database/photos-general.py
fi

echo; echo "Everything is done! Launching the server..."; echo
./manage.py runserver
