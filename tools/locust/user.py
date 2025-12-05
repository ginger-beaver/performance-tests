from locust import User, between

from config import settings


class LocustBaseUser(User):
    host: str = "localhost"
    abstract = True
    wait_time = between(
        min_wait=settings.locust_user.wait_time_min,
        max_wait=settings.locust_user.wait_time_max
    )
