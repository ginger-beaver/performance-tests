from locust import User, between


class LocustBaseUser(User):
    host: str = "localhost"
    abstract = True
    wait_time = between(1, 3)
