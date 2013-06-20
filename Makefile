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
	@cd examplesite && python manage.py test

run: clean
	@cd examplesite && python manage.py syncdb
	@cd examplesite && python manage.py migrate
	@cd examplesite && python manage.py runserver
