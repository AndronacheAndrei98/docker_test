# Day 1 - Task 1 Solution

## Issue Found
I tried to build the Dockerfile buit it gave the following error:
"
Dockerfile:4
--------------------
   2 |
   3 |
   4 | >>> WORKDIR /usr/share/nginx/html
   5 |
   6 |     COPY index.html .
--------------------
ERROR: failed to solve: no build stage in current context
"

## Solution
Upon inspecting the Dockerfile, I could observe that there is no "FROM" line.
I looked for the base docker image for "nginx" in DockerHub and added the following line at the beginning:
"
FROM nginx
"
Then it worked fine.

## Commands Used
```bash
docker build -t day1-task1 .
docker build -t day1-task1 .
```

## Lessons Learned
You should always check the validity of Dockerfiles before thinking of more "advanced" issues and fixes.
Basically all "parts" should be there.