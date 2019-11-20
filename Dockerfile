FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
CMD python3.6 /app/manage.py runserver 0.0.0.0:8000
