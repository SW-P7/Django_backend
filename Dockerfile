FROM python:3.10.12


COPY ./webapp/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

#ENTRYPOINT ["python", "webapp/webapp/manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]
# Copy uwsgi.ini file
COPY uwsgi.ini /etc/uwsgi/

# The command to run uWSGI
CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
