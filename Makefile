install:
	pip install -r requirements.txt
test:
	python -m pytest -vv --cov=hello --cov=greeting tests

debug:
	# Debugger is invoked
	python -m pytest -vv --pdb

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

all: install lint test format
