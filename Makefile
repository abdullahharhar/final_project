.PHONY: test venv clean

venv:
    python3 -m venv venv

install:
    venv/bin/pip install -r requirements.txt

test:
    venv/bin/python -m pytest --tb=short

clean:
    rm -rf venv __pycache__ .pytest_cache *.pyc *_concat* *_concat_many
