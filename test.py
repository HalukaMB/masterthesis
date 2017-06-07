from redis import Redis

from rq import Queue

import time

import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


q = Queue(connection=Redis())
job = q.enqueue(operator.add, 2, 3)

time.sleep(1)
print(job.result)
