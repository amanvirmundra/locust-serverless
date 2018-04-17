import sys, os.path
import json
from argparse import Namespace
from locust import runners
import locustfile

# read request data
postreqdata = json.loads(open(os.environ['req']).read())
baseurl = postreqdata['url']
hatch_rate = postreqdata['hatch_rate']
num_requests = postreqdata['num_requests']

# set options and trigger tests
options = Namespace()
options.host = baseurl
options.num_clients = 5
options.hatch_rate = hatch_rate
options.num_requests = num_requests
options.no_reset_stats = True

runners.locust_runner = runners.LocalLocustRunner([locustfile.WebsiteUser], options)
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