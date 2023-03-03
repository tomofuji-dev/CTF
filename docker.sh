docker container run -it -d --name ctfub --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" --platform=linux/amd64 -v /Users/t.fuji/Dev/42/cursus/.playground/CpawCTF:/CpawCTF ubuntu:latest
docker container exec -it ctfubuntu /bin/bash
