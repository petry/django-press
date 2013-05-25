help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'

clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt
	@pip install -r requirements_test.txt

setup: deps


test_functional: clean
	@echo "running functional tests..."
	@cd examplesite && python manage.py test

test_unit: clean
	@echo "running unit tests..."
	@nosetests -s  --with-coverage --cover-package=press

test: deps test_unit test_functional
