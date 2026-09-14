"""Optional: uses only a learner-started dedicated Redis at REDIS_URL."""
import os
from redis import Redis
from rq import Queue, Retry
from rq_task import count_words
if __name__ == "__main__":
    connection = Redis.from_url(os.environ.get("REDIS_URL", "redis://127.0.0.1:6386/0"))
    job = Queue("week6", connection=connection).enqueue(
        count_words, "queues carry job references", retry=Retry(max=2, interval=[5, 10]))
    print(job.id)
    print(job.get_status())
