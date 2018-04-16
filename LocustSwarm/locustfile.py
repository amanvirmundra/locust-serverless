import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myvenv/Lib/site-packages')))
from locust import HttpLocust, TaskSet, task

# read request data
postreqdata = json.loads(open(os.environ['req']).read())
baseurl = postreqdata['url']
hatch_rate = postreqdata['hatch_rate']
num_requests = postreqdata['num_requests']

# define locust tasks
class Task(TaskSet):
    @task()
    def get_home_page(self):
        response = self.client.get("/")
        print("Response status code:", response.status_code)

class WebsiteUser(HttpLocust):
    task_set = Task
