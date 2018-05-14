web: gunicorn wger.wsgi:application --log-file -
release: python manage.py makemigrations --merge $$ python manage.py migrate

