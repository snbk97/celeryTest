import sqlite3
from time import sleep
from celery import Celery
from time import sleep

connection = sqlite3.connect('test.sqlite', check_same_thread=False, timeout=10, isolation_level=None)
cursor = connection.cursor()

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def updateResult(id, number1, number2):
    sum = number1 + number2
    sleep(10)
    cursor.execute("UPDATE sums SET answer = ? WHERE id = ?", (sum, id))
