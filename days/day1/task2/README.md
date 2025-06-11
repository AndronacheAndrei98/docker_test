# Task 2: Incorrect Port Exposure

## Objective
Fix the Dockerfile so the web server is accessible.

## Instructions
1. Build the image using: `docker build -t day1-task2 .`
2. Run the container using: `docker run -p 8080:80 day1-task2`
3. Try to access http://localhost:8080 in your browser
4. It won't work! Identify what's wrong with the Dockerfile
5. Fix the issue
6. Rebuild and run the container again
7. Verify it works by accessing http://localhost:8080

## What to Submit
Document the issue you found and how you fixed it in the solutions/day1/task2.md file. 