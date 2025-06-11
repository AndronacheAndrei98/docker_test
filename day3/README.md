# Day 3: Multi-Container Communication

## Objective
Debug and fix issues in a multi-container application with a web service and a database.

## Instructions
1. Examine the `docker-compose.yml` file and the application files
2. Run the application using: `docker-compose up`
3. The web service will not be able to connect to the database
4. Use `docker-compose logs` to see the errors
5. Fix the issues in the configuration files
6. Run the application again to verify it works
7. Access the web application at http://localhost:8080

## What to Look For
- Network communication issues between containers
- Incorrect configuration of environment variables
- Volume mounting problems
- Logging configuration issues

## What to Submit
Document all issues you found and how you fixed them in the solutions/day3/solution.md file. 