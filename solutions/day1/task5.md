# Day 1 - Task 5 Solution

## Issue Found
During the build phase I got the following error:
```bash
 => ERROR [3/5] COPY requirements.txt .                                                                                                                                                                                                             0.0s 
------
 > [3/5] COPY requirements.txt .:
------
Dockerfile:6
--------------------
   4 |
   5 |
   6 | >>> COPY requirements.txt .
   7 |     RUN pip install -r requirements.txt
   8 |
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref g3v37davkm4m9o2zjo672v553::jw5npo2wmp4o51pfh0abl1oc0: "/requirements.txt": not found
```

## Solution
From what I can see the "requirements.txt" file is missing. The one used in the "RUN pip install -r requirements.txt" part
Created the file and everything worked:
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day1\task5> docker run -p 8080:8080 day1-task5
172.17.0.1 - - [11/Jun/2025 18:29:47] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [11/Jun/2025 18:29:47] "GET /favicon.ico HTTP/1.1" 200 -
Serving at port 8080
Traceback (most recent call last):
  File "/app/app.py", line 49, in <module>
    httpd.serve_forever()
```

## Commands Used
```bash
docker build -t day1-task5 .
docker run -p 8080:8080 day1-task5
docker build -t day1-task5 .
docker run -p 8080:8080 day1-task5
```

## Lessons Learned
I learned that we should check that all required files are present in the build folder when we are building a Dockerfile.
I also learned that most errors in Docker tell me exactly what the issue is if I look.