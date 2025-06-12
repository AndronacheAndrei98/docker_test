# Day 2 - Task 1 Solution

## Issue Found
When running the container we get the following error:
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day2\task2> docker run day2-task2
Starting application...
Reading data from data.txt...
ERROR: Invalid data format in data.txt - invalid literal for int() with base 10: 'invalid'
The file should contain only numbers, one per line.
```

## Logs Analyzed
```bash
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day2\task2> docker run day2-task2
Starting application...
Reading data from data.txt...
ERROR: Invalid data format in data.txt - invalid literal for int() with base 10: 'invalid'
The file should contain only numbers, one per line.
```

## Solution
While looking at the log above I can see the folowing:
```bash
ERROR: Invalid data format in data.txt - invalid literal for int() with base 10: 'invalid'
The file should contain only numbers, one per line.
```
In the "data.txt" file and I could see the "invalid" entry.
Since the python code only knows to parse numbers, it crashed.
The part that crashes is the one that convers string to int:
```bash
value = int(line.strip())
```
To fix this we can replace or remove the "invalid" entry:
```bash
10
20
30
invalid -> 40
50 
```
After that it worked fine:
```bash
Starting application...
Reading data from data.txt...
Data processed successfully! Total: 150

==================================================
SUCCESS! You've fixed the crashing container issue!
The application needed valid numeric data in data.txt.
==================================================
```

## Commands Used
```bash
docker build -t day2-task2 .
docker run day2-task2
```

## Lessons Learned
I learned that we should check that the validity of the files and data being used in the docker build process, since if you receive the already built image without the dockerfile, there would be no easy way to fix it quickly.
