# Day 1 - Task 4 Solution

## Issue Found
When running the container we get the following error:
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day1\task4> docker run -p 8080:3000 day1-task4
Usage: npm <command>
where <command> is one of:
.....
Specify configs in the ini-formatted file:
    /root/.npmrc
or on the command line via: npm <command> --key value
Config info can be viewed via: npm help config

npm@6.14.18 /usr/local/lib/node_modules/npm
```

## Solution
Since I could see that the command docker has an issue with, is not the command running during the build (It would have given an error during the build phase), I looked into the "CMD" part that only runs during "docker run".
Since the error complained that the command is not present in the list of known commands, I searched online and found out that "npm start" is the command that is used, and that exists.
I replaced "npm start-server" with "npm start"

## Commands Used
```bash
docker build -t day1-task4 .
docker run -p 8080:3000 day1-task4
docker build -t day1-task4 .
docker run -p 8080:3000 day1-task4
```

## Lessons Learned
I learned that its good to know what each step of the Dockerfile does since I would have spent more time investigating the "RUN npm install" part if I did not know that the CMD part only runs during the run part.