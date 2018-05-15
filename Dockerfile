ENV PYTHONBUFFERED 1
WORKDIR /code
COPY requirements* ./
RUN pip install -r requirements_devel.txt
RUN pip install -e git+https://github.com/andela/wg-bigas-opus.git@177eeae62d3d56019d788afcee3972f5ac3a9606#egg=wger
RUN apt-get update && apt-get install -y nodejs nodejs-legacy npm libjpeg62-turbo-dev zlib1g-dev vim tmux
COPY . .
RUN wger create-settings  --settings-path `pwd`/wger/settings.py  --database-path `pwd`/database.sqlite
RUN wger bootstrap-wger --settings-path `pwd`/wger/settings.py  --no-start-server
CMD python manage.py runserver 0.0.0.0:8000 --settings=wger.settings