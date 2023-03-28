docker container run -it -d --name ctfubuntu --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" -v /Users/t.fuji/Dev/42/learning/CTF:/CTF ubuntu:latest
docker container exec -it ctfubuntu /bin/bash
