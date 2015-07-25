# -*- coding: utf-8 -*-
from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app = Celery('hello', broker=BROKER_URL)
