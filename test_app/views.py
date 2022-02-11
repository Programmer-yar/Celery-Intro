from django.shortcuts import render
from tasks import test_func
import time
# Create your views here.

def home(request):
    test_func.delay()
    return render(request, 'test_app/home.html')

# @app.task
# def test_func():
#     print("delay started!")
#     time.sleep(5)
#     print("delay ended!")