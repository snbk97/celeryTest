# celery Demo

Steps to run:

Make sure python and pip installed 

Make sure redis is installed in your system

`poetry install`

Start celery worker

`celery -A tasks worker --loglevel=info`

`python app.py`
