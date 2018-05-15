web: gunicorn wger.wsgi:application --log-file -
release: docker build -t wger_dev . && docker run wger_dev
