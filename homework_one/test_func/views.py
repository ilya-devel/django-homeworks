from django.shortcuts import render
from django.http import HttpResponse
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def write_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'{func.__name__} launched')
        return func(*args, **kwargs)
    return wrapper


# Create your views here.
@write_log
def hello(request):
    return HttpResponse('<h1>HELLO</h1>')