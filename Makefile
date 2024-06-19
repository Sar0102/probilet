tag=latest
organization=sarik0102
image_name=probilet_backend_repo


build:
	docker build --force-rm -t sarik0102/probilet_backend_repo .

run:
	python manage.py runserver 0.0.0.0:9000

push:
	docker tag $(organization)/$(image_name):latest $(organization)/$(image_name):$(tag)
	docker push $(organization)/$(image_name):$(tag)

start-server:
	python manage.py runserver 0.0.0.0:80
