import time
from locust import HttpUser, TaskSet, task, between

class CallerActions(TaskSet):
    wait_time = between(1, 2)

    @task
    def index(self):
        self.client.get("/")

    @task
    def get_prediction(self):
        self.client.get("/predictions")

class APIUser(HttpUser):
    task_set = CallerActions
    min_wait = 5000
    max_wait = 9000