FROM python:3.7.2

RUN pip install --upgrade pip uwsgi virtualenv
RUN virtualenv -p python3 --no-site-packages /jjanhaeyo/venv

RUN apt-get update && apt-get install netcat-openbsd supervisor nginx vim -y

WORKDIR /jjanhaeyo/

COPY ./requirements/ /jjanhaeyo/requirements/
RUN /jjanhaeyo/venv/bin/pip install -r requirements/prod.txt

COPY ./.docker/ /jjanhaeyo/.docker/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /jjanhaeyo/.docker/jjanhaeyo_nginx.conf /etc/nginx/sites-enabled/jjanhaeyo

RUN mkdir -p /var/log/jjanhaeyo/
RUN mkdir -p /var/log/jjanhaeyo_tasks/
RUN touch /var/log/jjanhaeyo/jjanhaeyo_access.log
RUN touch /var/log/jjanhaeyo/jjanhaeyo_error.log

COPY . /jjanhaeyo/

EXPOSE 8000
CMD ["/jjanhaeyo/.docker/run.sh"]
