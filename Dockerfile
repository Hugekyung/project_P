FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Hugekyung/project_P.git

WORKDIR /home/project_P/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=u+cq5&1je+l*18j51n7d28^beykb7hr^xg+tujjm4=90)p(q2+" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]