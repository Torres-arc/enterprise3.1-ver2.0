# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 9:43
# @Author  : Torres
# @File    : timer.py

from runner import MainPage
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


jobstores = {
    'default': MemoryJobStore()
}
executors = {
     'default': ThreadPoolExecutor(20),
     'processpool': ProcessPoolExecutor(10)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(MainPage.creat, trigger='cron', hour=12, minute=25)
try:
    scheduler.start()
except SystemExit:
    print('exit')
    exit()