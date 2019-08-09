init:
	python jjanhaeyo/manage.py migrate

test:
	pytest jjanhaeyo/

superuser:
	python jjanhaeyo/manage.py createsuperuser

flush:
	mysql -u root -e 'DROP DATABASE jjanhaeyo; CREATE DATABASE jjanhaeyo CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;'

reset: flush init

run:
	python jjanhaeyo/manage.py runserver

shell:
	python jjanhaeyo/manage.py shell -i bpython

migrate:
	python jjanhaeyo/manage.py makemigrations --merge
	python jjanhaeyo/manage.py makemigrations
	python jjanhaeyo/manage.py migrate

docker_build:
	git rev-parse HEAD > version
	docker build -t jjanhaeyo-server .

docker_login:
	$$(aws ecr get-login --no-include-email)

docker_run: docker_down docker_build
	docker-compose up

docker_down:
	docker-compose down
