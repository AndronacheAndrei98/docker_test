# Day 3 - Multi-Container Solution

## Issues Found

1. Issue: 
   "Web" service cannot connect to the "DB" postgres service.
   
   Solution:
   This is because the port used by the "web" service to connect to the "db" service is wrong.
   By default postgres uses port "5432"
   Changed the env variable to be the following:
   ```bash
      - DATABASE_PORT=5432
   ```

2. Issue:
   The attribute "version" is now obsolete.
   ```bash
   "version: '3'"
   ```
   Solution:
   I removed it since it did not do anything.

3. Extra additions:
Added "depends_on" attribute. This is so compose always starts and stops containers in dependency order(https://docs.docker.com/compose/how-tos/startup-order/).

   Solution:
Added the following to the Docker compose file:
   ```bash
   depends_on:
       - db
   ```
This is not required, but it is useful because it makes sure the "db" service is started first before starting the "web" service

4. Extra additions:
Created a custom bridge network called app-network and assigned both services to it for proper container communication so that the containers work, but do not use the default network, reflecting a more realistic approach.
Each network got the following line
   ```bash
   networks:
      - app-network
   ```
And we created the following network:
   ```bash
   app-network:
      driver: bridge
   ```
This is not required, since it worked fine with the default network, but again it reflects a more "similar to onprem" approach.

5. Extra additions:
Checking that volumes work fine.
Checking that volumes work fine as well.
Added adminer service to connect to database and test the persistent volume by changing the values in the list:
   ```bash
 adminer:
    image: adminer
    restart: always
    ports:
      - 8000:8080
   ```
Worked fine, demonstrated that the volume works ok, and logging as well:
   ```bash
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 Accepted                                                                                                                                                                               
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 [200]: GET /?pgsql=db&username=postgres&db=app_db&ns=public&select=items                                                                                                               
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 Closing
   ```
Basically I deleted the first entry in the table, and after using "docker compose down", and the "docker compose up" the entry remained deleted.

## Logs Analyzed
```
time="2025-06-13T10:21:32+03:00" level=warning msg="C:\\Users\\ZZ03GR826\\Documents\\GitHub\\docker_test\\day3\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
unable to get image 'day3-web': error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.49/images/day3-web/json": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```
```
web-1     | Web service listening at http://localhost:3000                                                                                                                                                                                               
web-1     | Environment variables:
web-1     | DATABASE_HOST: postgres                                                                                                                                                                                                                      
web-1     | DATABASE_PORT: 5432                                                                                                                                                                                                                          
web-1     | DATABASE_USER: postgres                                                                                                                                                                                                                      
web-1     | DATABASE_NAME: app_db
web-1     | Attempting to connect to database with config: {                                                                                                                                                                                             
web-1     |   host: 'postgres',                                                                                                                                                                                                                          
web-1     |   port: '5432',                                                                                                                                                                                                                              
web-1     |   database: 'app_db',
web-1     |   user: 'postgres'                                                                                                                                                                                                                           
web-1     | }                                                                                                                                                                                                                                            
web-1     | Successfully connected to database!                                                                                                                                                                                                          
web-1     | Attempting to connect to database with config: {
web-1     |   host: 'postgres',
web-1     |   port: '5432',                                                                                                                                                                                                                              
web-1     |   database: 'app_db',                                                                                                                                                                                                                        
web-1     |   user: 'postgres'                                                                                                                                                                                                                           
web-1     | }
web-1     | Successfully connected to database!                                                                                                                                                                                                          
web-1     | Attempting to connect to database with config: {                                                                                                                                                                                             
web-1     |   host: 'postgres',
web-1     |   port: '5432',                                                                                                                                                                                                                              
web-1     |   database: 'app_db',                                                                                                                                                                                                                        
web-1     |   user: 'postgres'
web-1     | }                                                                                                                                                                                                                                            
web-1     | Successfully connected to database!  
```
```
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 Accepted                                                                                                                                                                               
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 [200]: GET /?pgsql=db&username=postgres&db=app_db&ns=public&select=items                                                                                                               
adminer-1  | [Fri Jun 13 08:24:06 2025] [::ffff:172.18.0.1]:47502 Closing
```

```
web-1      | Web service listening at http://localhost:3000
web-1      | Environment variables:
web-1      | DATABASE_HOST: db                                                                                                                                                                                                                           
web-1      | DATABASE_PORT: 5                                                                                                                                                                                                                            
web-1      | DATABASE_USER: postgres                                                                                                                                                                                                                     
web-1      | DATABASE_NAME: app_db                                                                                                                                                                                                                       
web-1      | Attempting to connect to database with config: { host: 'db', port: '5', database: 'app_db', user: 'postgres' }
web-1      | Database connection error: connect ECONNREFUSED 172.18.0.3:5
```

## Commands Used
```bash
docker compose up
docker compose logs
docker network ls
docker compose down
docker container ls
docker image ls
docker container rm
docker image rm
docker logs
docker volume ls
docker volume rm
```

## Docker Compose Changes

Changed the port env variable to be the following:
   ```yaml
      - DATABASE_PORT=5432
   ```

The attribute "version" is obsolete, and I removed it:
   ```yaml
   "version: '3'"
   ```


Created a custom bridge network called app-network and assigned both services.
Each network got the following line:
   ```yaml
   networks:
      - app-network
   ```
And we created the following network:
   ```yaml
   app-network:
      driver: bridge
   ```

Added the following to the Docker compose file:
   ```yaml
   depends_on:
       - db
   ```
Added adminer service to connect to database and test the persistent volume by changing the values in the list:
   ```bash
 adminer:
    image: adminer
    restart: always
    ports:
      - 8000:8080
   ```
This also helped test logging.

## Lessons Learned
I learned about persistent volumes, and how to use them properly.
I learned about logging, and how different setups for it work.
I learned about correct port usage, and network creation in docker.
I learned how to debug using the docker compose logs.