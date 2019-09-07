#!/usr/bin/env bash

cd /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1
docker build -t phase1_docker:latest . > logfile.txt
docker ps >> logfile.txt
docker run -d -p 9001:5000 phase1_docker:latest >> logfile.txt
docker ps >> logfile.txt