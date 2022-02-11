from celery import Celery
import time

""" Celery('current_module_name', backend='', broker='')
- broker(Input) => specifies the message broker to use e.g RabbitMQ, redis
- backend(Output) => used to specify a backend for storing states/results
  of tasks. This is optional.
"""
# app = Celery(
# 	'tasks', backend='redis://localhost', broker='redis://localhost')

app = Celery('tasks', broker='redis://localhost')

@app.task
def add(x, y):
	return x + y

@app.task
def test_func():
    print("delay started!")
    time.sleep(5)
    print("delay ended!")
    return "Ended!"
# def test_run():
# 	result = add.delay(11, 11)
# 	print(result.ready())
# 	print(result.get())
# 	print(result.ready())