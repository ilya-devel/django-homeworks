import logging

logger = logging.getLogger(__name__)


def write_log(func):
    def wrapper(*args, **kwargs):
        logger.info(f'{func.__name__} launched')
        return func(*args, **kwargs)
    return wrapper
