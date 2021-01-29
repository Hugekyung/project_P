FROM python:3.9.0

WORKDIR /home/

RUN echo "testing13"

RUN git clone https://github.com/Hugekyung/project_P.git

WORKDIR /home/project_P/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=project_P.settings.deploy && python manage.py migrate --settings=project_P.settings.deploy && gunicorn project_P.wsgi --env DJANGO_SETTINGS_MODULE=project_P.settings.deploy --bind 0.0.0.0:8000"]