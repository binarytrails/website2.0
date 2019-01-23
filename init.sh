git submodule init
git submodule update
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
./manage.py runserver
