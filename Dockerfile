# Mount the ubuntu picture
FROM ubuntu:latest

# Mount the folder "code"
ADD . /code

# Define the working folder
WORKDIR /code

# Installations
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install postgresql-client python3 python3-pip nginx libpq-dev -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install Flask Flask-Login Flask-SQLAlchemy Flask-CLI psycopg2 sqlalchemy_utils

# Export locals to use UTF-8
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

# Execute command
CMD ["python3", "pageStatus/run_server.py"]
