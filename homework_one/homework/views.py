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


@write_log
def index(request):
    html = """
    <h1>HOME PAGE</h1>
    <p>This is simple home page for example</p>
"""
    return HttpResponse(html)
