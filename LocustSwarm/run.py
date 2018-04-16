import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myvenv/Lib/site-packages')))
import json
from argparse import Namespace
from locust import HttpLocust, TaskSet, task, runners

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

# set options and trigger tests
options = Namespace()
options.host = baseurl
options.num_clients = 5
options.hatch_rate = hatch_rate
options.num_requests = num_requests
options.no_reset_stats = True

runners.locust_runner = runners.LocalLocustRunner([WebsiteUser], options)
runners.locust_runner.start_hatching(wait=True)
runners.locust_runner.greenlet.join()

response = open(os.environ['res'], 'w')
results = []

for name, value in runners.locust_runner.stats.entries.items():
    data = {}
    data['url'] = name
    data['min_response_time'] = value.min_response_time
    data['median_response_time'] = value.median_response_time
    data['max_response_time'] = value.max_response_time
    data['total_rps'] = value.total_rps
    results.append(data)

stats = json.dumps(results)
response.write(stats)
response.close()
