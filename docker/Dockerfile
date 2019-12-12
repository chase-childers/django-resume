FROM python:3.5

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y nginx vim
RUN pip install pipenv
RUN mkdir /srv/logs
COPY . /application
WORKDIR /application

# COPY ./nginx/django_nginx.conf /etc/nginx/sites-available/
COPY ./nginx/django_nginx.conf /etc/nginx/conf.d/default.conf    
# RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled
RUN pipenv install --system --deploy --ignore-pipfile
RUN service nginx stop
RUN nginx -t 
ENTRYPOINT scripts/entrypoint.sh
