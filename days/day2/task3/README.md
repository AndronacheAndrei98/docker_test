# Task 3: Resource Constraints

## Objective
Identify and fix a resource constraint issue in a container.

## Instructions
1. Build the image: `docker build -t day2-task3 .`
2. Run the container: `docker run day2-task3`
3. The application will start but then become unresponsive
4. Use `docker stats` to monitor the container's resource usage
5. Fix the issue by running the container with appropriate resource limits
6. Verify the container runs successfully

## Hint
This task is about memory constraints. You'll need to run the container with memory limits.

## What to Submit
Document the issue you found, the resource metrics you observed, and how you fixed it in the solutions/day2/task3.md file. 