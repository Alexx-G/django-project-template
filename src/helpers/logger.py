import logging
try:
    from django.conf import settings
except ImportError as e:
    print("Can't import django settings.")
    settings = None


def get_logger(logger_name, autoprefix=True):
    if autoprefix and settings and hasattr(settings, 'SITE_NAME'):
        logger_name = "{0}.{1}".format(settings.LOGGING_ROOT, logger_name)
    return logging.getLogger(logger_name)
