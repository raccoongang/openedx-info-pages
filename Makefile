.PHONY: requirements test

requirements:
	pip install -r requirements/test.txt

tests:
	pytest
