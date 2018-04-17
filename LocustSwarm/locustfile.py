import sys, os.path
from locust import HttpLocust, TaskSet, task

# define locust tasks
class Task(TaskSet):
    @task()
    def get_home_page(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = Task
