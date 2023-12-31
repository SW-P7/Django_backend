# Use the official Python image as the base image
FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY webapp/requirements.txt /app/

# Install dependencies
RUN apt-get update && apt-get install -y iproute2
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000

COPY uwsgi.ini /etc/uwsgi/
# Run the Django development server
#CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]

CMD ["python", "manage.py" "runserver"]


