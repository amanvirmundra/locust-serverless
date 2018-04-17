# Locust Serverless
This app provides a quick and easy way to run [Locust](https://locust.io/) based load tests on Azure Cloud (Azure Functions).

All the resources required to run a function app are deployed by the ARM template. The deployment uses site extensions to install a custom python runtime and setup code deployment from this github repository. Once everything is deployed succesfully, you will have an API endpoint which can be used to trigger an ad-hoc load test.

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

### Example
#### Request
```
POST https://<your_app_name>.azurewebsites.net/api/LocustSwarm
{
    "url": "http://www.example.com",
    "hatch_rate": 1,
    "num_requests": 10
}
```
#### Response
```json
[
    {
        "url": [
            "/",
            "GET"
        ],
        "min_response_time": 93,
        "median_response_time": 98,
        "max_response_time": 1296,
        "total_rps": 3.6185047752716208
    }
]
```

## Locust
[Locust](https://locust.io/) is an open source load testing tool. It uses a simple python based code to define user behaviour and can be used to swarm host applications/websites with millions of simultaneous users. 

## Azure Functions (Serverless computing)
[Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) provide a quick way to run small pieces of code on a highly scalable cloud infrastructure.  

## ARM Template
ARM template ([azuredeploy.json](https://github.com/amanvirmundra/locust-serverless/blob/master/azuredeploy.json)) deploys all the resources required to setup an Azure Function:
- App Service Plan (Consumption plan): Azure functions have a default timeout of 5 mins, which can be increased to upto 10 mins (as of writing this). If you to run your tests for a longer duration then choose a Fixed App Service plan.
- Function App
- Storage Account

## References
- [invokust](https://github.com/FutureSharks/invokust): Gives you a way to run Locust on AWS Lambda
- Fully automated Azure Functions deployment using Python (https://github.com/meken/azure-functions-python)




