# Day 2 - Task 1 Solution

## Issue Found
By using the "docker stats" command we could see that the memory usage was rising quickly:
```bash
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O       PIDS
c1a4224b444a   sad_buck   9.74%     3.382GiB / 15.5GiB   21.82%    1.17kB / 126B   6.5MB / 193kB   1
```
to
```bash
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O       PIDS
c1a4224b444a   sad_buck   8.49%     13.17GiB / 15.5GiB   84.99%    1.17kB / 126B   6.5MB / 193kB   1
```
After reaching the limit it crashed the container:
```bash
Allocated 18120.00 MB of memory
Allocated 18130.00 MB of memory
PS C:\Users\ZZ03GR826\Documents\GitHub\docker_test\day2\task3> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Logs Analyzed
```bash
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O       PIDS
c1a4224b444a   sad_buck   9.74%     3.382GiB / 15.5GiB   21.82%    1.17kB / 126B   6.5MB / 193kB   1
```
```bash
CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O       PIDS
c1a4224b444a   sad_buck   9.74%     3.382GiB / 15.5GiB   21.82%    1.17kB / 126B   6.5MB / 193kB   1
```
```bash
Allocated 18010.00 MB of memory
Allocated 18020.00 MB of memory
Allocated 18030.00 MB of memory
Allocated 18040.00 MB of memory
Allocated 18050.00 MB of memory
Allocated 18060.00 MB of memory
Allocated 18070.00 MB of memory
Allocated 18080.00 MB of memory
Allocated 18090.00 MB of memory
Allocated 18100.00 MB of memory
Allocated 18110.00 MB of memory
Allocated 18120.00 MB of memory
Allocated 18130.00 MB of memory
```

## Solution
The solution is to use docker resource constraints like this:
```bash
docker run --memory=150m day2-task3
```

After that it did not crash anymore.
There are multiple constraints documented here: https://docs.docker.com/engine/containers/resource_constraints/

There was also an issue regarding the python script itself.
The issue was that the script only used the location for cgroups v1 "/sys/fs/cgroup/memory/memory.limit_in_bytes".
Docker right now uses cgroups v2, and sets the memory limit in "/sys/fs/cgroup/memory.max" when running the docker run command with the memory option.
I tried several options, but none worked since the location "/sys/fs/cgroup/" is a restricted location, where no files can be created, and no permissions can be changed.
Tehnically the running cgroup version can be changed as described here "https://docs.docker.com/engine/containers/runmetrics/", but seems like it does not work great with docker on windows.
We replaced the script with one that also includes an option for cgroups v2, and after that the container worked great:
```bash
==================================================
SUCCESS! You've set appropriate memory limits!
The container now runs without crashing.
==================================================
```

## Commands Used
```bash
docker build -t day2-task3 .
docker run day2-task3
docker stats
docker run --memory=150m day2-task3
docker stats
docker run --name test --rm --memory=150m -d day2-task3
docker logs -f test
docker exec -it test cat /sys/fs/cgroup/memory.max
```

## Lessons Learned
I learned how to use "docker stats" to monitor the resources used by docker containers, and docker resource constraints to set limits on those resources.
I also learned a lot about where the docker resource constraints are set in the docker container itself during the docker run phase.
This also included information about how docker can use cgroups v2 or cgroups v1 to set those parameters or limits.