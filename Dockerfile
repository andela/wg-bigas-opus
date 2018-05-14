
FROM python:3
ENV PYTHONBUFFERED 1
WORKDIR /code
COPY requirements* ./
RUN pip install -r requirements_devel.txt
RUN pip install wger
RUN apt-get update && apt-get install -y nodejs nodejs-legacy npm libjpeg62-turbo-dev zlib1g-dev vim tmux
COPY . .
RUN python manage.py setup develop
RUN wger bootstrap-wger
CMD python manage.py makemigrations --merge && python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000 --settings=wger.settings
