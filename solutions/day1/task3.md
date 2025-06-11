# Day 1 - Task 1 Solution

## Issue Found
I get the following error when running the docker image I built:
"
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\days\day1\task3> docker run day1-task3
Traceback (most recent call last):
  File "/app/app.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
"
## Solution
I could see that the error mentions this:
"
  File "/app/app.py", line 1, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
"
I looked in the python file and I could see that the code uses an extra python module.
Since the python image does not contain the "Flask" module I looked up online on how to import it.
I added this part:
"
RUN pip install flask
"
I built the image again with the added command.
Image now builds successfuly but opening the address does not work:
"
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day1\task3> docker run day1-task3        
Starting Flask application...
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
"

Since the port used is not exposed, I had to add it to the "docker run command" and it then worked:
"
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day1\task3> docker run -p 5000:5000 day1-task3 
Starting Flask application...
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [11/Jun/2025 12:45:06] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [11/Jun/2025 12:45:07] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [11/Jun/2025 12:45:57] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [11/Jun/2025 12:45:57] "GET /favicon.ico HTTP/1.1" 404 -
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day1\task3> 
"
I also added an "expose" part to the Dockerfile so that it is documented which port needs to be exposed:
"
EXPOSE 5000
"

## Commands Used
```bash
docker build -t day1-task3 .
docker run day1-task3
docker build -t day1-task3 .   
docker run -p 5000:5000 day1-task3 
```

## Lessons Learned
I learned that when building a Dockerfile we must take into account all the dependecies that are needed in order for the container to run.