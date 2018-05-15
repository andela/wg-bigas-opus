web: gunicorn wger.wsgi:application --log-file -
release: docker build -t wger_dev . && docker run -p 8000:8000 wger_dev
