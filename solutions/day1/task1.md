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

## Commands Used
```bash
docker build -t day1-task1 .
[+] Building 0.9s (8/8) FINISHED                                                      docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                  0.0s
 => => transferring dockerfile: 181B                                                                  0.0s 
 => [internal] load metadata for docker.io/library/nginx:latest                                       0.6s 
 => [internal] load .dockerignore                                                                     0.0s
 => => transferring context: 2B                                                                       0.0s 
 => [1/3] FROM docker.io/library/nginx:latest@sha256:6784fb0834aa7dbbe12e3d7471e69c290df3e6ba810dc38  0.0s 
 => => resolve docker.io/library/nginx:latest@sha256:6784fb0834aa7dbbe12e3d7471e69c290df3e6ba810dc38  0.0s 
 => [internal] load build context                                                                     0.0s 
 => => transferring context: 32B                                                                      0.0s 
 => CACHED [2/3] WORKDIR /usr/share/nginx/html                                                        0.0s 
 => CACHED [3/3] COPY index.html .                                                                    0.0s
 => exporting to image                                                                                0.1s 
 => => exporting layers                                                                               0.0s 
 => => exporting manifest sha256:4ce5f0c56aad7652a81b84ad2b3d57692a56168954528721f05f619c2a8bf8d3     0.0s 
 => => exporting config sha256:a330ba4da2777d5e5a56ea948b73be3fceddb6508103477c287a74417102a680       0.0s 
 => => exporting attestation manifest sha256:497668de33e5a6621ddeee9767597448f386e195d621f2ff83fbee4  0.0s 
 => => exporting manifest list sha256:fb479531e94f69959ab7c6a72981dde483b9cd285c8fb743cad166e02db46c  0.0s 
 => => naming to docker.io/library/day1-task1:latest                                                  0.0s 
 => => unpacking to docker.io/library/day1-task1:latest                                               0.0s 
PS C:\Users\ZZ03GR826\Documents\GitHub\network_test\config\configDB\assignment2\assignment2\days\day1\task1> docker run -p 8080:80 day1-task1
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/06/11 11:52:14 [notice] 1#1: using the "epoll" event method
2025/06/11 11:52:14 [notice] 1#1: nginx/1.27.5
2025/06/11 11:52:14 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2025/06/11 11:52:14 [notice] 1#1: OS: Linux 6.6.87.1-microsoft-standard-WSL2
2025/06/11 11:52:14 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/06/11 11:52:14 [notice] 1#1: start worker processes
2025/06/11 11:52:14 [notice] 1#1: start worker process 29
2025/06/11 11:52:14 [notice] 1#1: start worker process 30
2025/06/11 11:52:14 [notice] 1#1: start worker process 31
2025/06/11 11:52:14 [notice] 1#1: start worker process 32
2025/06/11 11:52:14 [notice] 1#1: start worker process 33
2025/06/11 11:52:14 [notice] 1#1: start worker process 34
2025/06/11 11:52:14 [notice] 1#1: start worker process 35
2025/06/11 11:52:14 [notice] 1#1: start worker process 36
2025/06/11 11:52:14 [notice] 1#1: start worker process 37
2025/06/11 11:52:14 [notice] 1#1: start worker process 38
2025/06/11 11:52:14 [notice] 1#1: start worker process 39
2025/06/11 11:52:14 [notice] 1#1: start worker process 40
172.17.0.1 - - [11/Jun/2025:11:52:20 +0000] "GET / HTTP/1.1" 200 677 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0" "-"
2025/06/11 11:52:21 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [11/Jun/2025:11:52:21 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0" "-"
2025/06/11 12:01:35 [notice] 1#1: signal 2 (SIGINT) received, exiting
2025/06/11 12:01:35 [notice] 29#29: exiting
2025/06/11 12:01:35 [notice] 30#30: exiting
2025/06/11 12:01:35 [notice] 31#31: exiting
2025/06/11 12:01:35 [notice] 33#33: exiting
2025/06/11 12:01:35 [notice] 30#30: exit
2025/06/11 12:01:35 [notice] 29#29: exit
2025/06/11 12:01:35 [notice] 32#32: exiting
2025/06/11 12:01:35 [notice] 34#34: exiting
2025/06/11 12:01:35 [notice] 33#33: exit
2025/06/11 12:01:35 [notice] 31#31: exit
2025/06/11 12:01:35 [notice] 37#37: exiting
2025/06/11 12:01:35 [notice] 35#35: exiting
2025/06/11 12:01:35 [notice] 32#32: exit
2025/06/11 12:01:35 [notice] 34#34: exit
2025/06/11 12:01:35 [notice] 36#36: exiting
2025/06/11 12:01:35 [notice] 35#35: exit
2025/06/11 12:01:35 [notice] 37#37: exit
2025/06/11 12:01:35 [notice] 36#36: exit
2025/06/11 12:01:35 [notice] 39#39: exiting
2025/06/11 12:01:35 [notice] 39#39: exit
2025/06/11 12:01:35 [notice] 38#38: exiting
2025/06/11 12:01:35 [notice] 38#38: exit
2025/06/11 12:01:35 [notice] 40#40: exiting
2025/06/11 12:01:35 [notice] 40#40: exit
2025/06/11 12:01:35 [notice] 1#1: signal 14 (SIGALRM) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2025/06/11 12:01:35 [notice] 1#1: worker process 31 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2025/06/11 12:01:35 [notice] 1#1: worker process 29 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2025/06/11 12:01:35 [notice] 1#1: worker process 30 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2025/06/11 12:01:35 [notice] 1#1: worker process 32 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: worker process 33 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: worker process 34 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: worker process 36 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: worker process 40 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 38
2025/06/11 12:01:35 [notice] 1#1: worker process 38 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 35
2025/06/11 12:01:35 [notice] 1#1: worker process 35 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 37
2025/06/11 12:01:35 [notice] 1#1: worker process 37 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: signal 29 (SIGIO) received
2025/06/11 12:01:35 [notice] 1#1: signal 17 (SIGCHLD) received from 39
2025/06/11 12:01:35 [notice] 1#1: worker process 39 exited with code 0
2025/06/11 12:01:35 [notice] 1#1: exit
```

## Lessons Learned
You should always check the validity of Dockerfiles before thinking of more "advanced" issues.
Basically all "parts" should be there.