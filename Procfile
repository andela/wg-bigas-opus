web: gunicorn wger.wsgi --log-file - 
release: python manage.py makemigrations --merge && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
