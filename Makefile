install:
	pip install -r requirements.txt
test:
	python -m pytest -vv --cov=hello --cov=greeting tests

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

all: install lint test format
