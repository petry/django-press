help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'

clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements_test.txt
	@python setup.py develop

setup: deps

test: clean
	@echo "running tests..."
	@python manage.py test

run: clean
	@python manage.py syncdb
	@python manage.py migrate
	@python manage.py runserver
