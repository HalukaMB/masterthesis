from redis import Redis
from rq import Queue
import time

from HalukasCode import all
q = Queue(connection=Redis())

job = q.enqueue(all)

time.sleep(2)
