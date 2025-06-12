# Day 2 - Task 1 Solution

## Issue Found
When running the container we got the following error:
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day2\task1> docker run day2-task1
Starting application...
ERROR: Missing required environment variable: API_KEY
This application requires the API_KEY environment variable to be set.
Please run the container with: -e API_KEY=your_api_key
```

## Logs Analyzed
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day2\task1> docker run day2-task1
Starting application...
ERROR: Missing required environment variable: API_KEY
This application requires the API_KEY environment variable to be set.
Please run the container with: -e API_KEY=your_api_key
```

## Solution
As the message in the error log says, there is no API_KEY enviroment variable set.
The need for it can be observed also in the python file also.
Running the docker run command with the "-e" step fixes the issue:
```bash
docker run -e API_key=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe day2-task1
```
You can also add an "ENV" step in the dockerfile, but this would hard set the variable:
```bash
ENV API_KEY=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe
```
## Commands Used
```bash
docker run day2-task1
docker run -e API_key=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe day2-task1
```

## Lessons Learned
I learned about environment variables and how to set them:
 - In the "docker run" command using "-e" ,e.g.:
 ```bash
 docker run -e API_key=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe day2-task1
 ```
  - In the "docker build" phase by adding "ENV" to the dockerfile ,e.g.:
 ```bash
 ENV API_KEY=AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe
 ```
 