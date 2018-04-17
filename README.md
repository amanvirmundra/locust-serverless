# Locust Serverless
This script provides a quick and easy way to run [Locust](https://locust.io/) based load tests on Azure Cloud (Azure Functions).

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

## Locust
[Locust](https://locust.io/) is an open source load testing tool. It uses a simple python based code to define user behaviour and can be used to swarm host applications/websites with millions of simultaneous users. 

## Azure Functions (Serverless computing)
[Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) provide a quick way to run small pieces of code on a highly scalable cloud infrastructure.  

## ARM Template
ARM template ([azuredeploy.json](https://github.com/amanvirmundra/locust-serverless/blob/master/azuredeploy.json)) deploys all the resources required to setup an Azure Function:
- App Service Plan (Consumption plan): Azure functions have a default timeout of 5 mins, which can be increased to upto 10 mins (as of writing this). If you to run your tests for a longer duration then choose a Fixed App Service plan.
- Function App
- Storage Account




