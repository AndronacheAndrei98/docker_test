# Day 1 - Task 2 Solution

## Issue Found
After running the container, page is not up.

## Solution
I looked up online on which port does nginx server by default and saw that usually on "80"
The run command from the readme.md maps 8080(local):8080(inside container) where nothing is served.
For it to run it should be 8080(local):80(inside container).
After that it worked fine.
I also added the following:
```bash
EXPOSE 80
```
This is more for documentatian, since the "EXPOSE 80" does not directly do anything.

## Commands Used
```bash
docker build -t day1-task2 .
docker run -p 8080:8080 day1-task2
docker run -p 8080:80 day1-task2
```

## Lessons Learned
Ports inside the container need to be correctly mapped to the outside of the container in order for us to reach the service/app.