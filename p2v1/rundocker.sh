#!/usr/bin/env bash

#cd /Users/srinivasrishindra/Desktop/Fall_2018/Distributed_Systems/project2/phase1/phase1_docker
##docker build -t phase1_docker:latest . > /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/logfile.txt
##docker ps >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/logfile.txt
##
##docker run -d -p 5001:5000 phase1_docker:latest >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/logfile.txt
##
##docker ps >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/logfile.txt




cd /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1
docker build -t phase1_docker:latest . > /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/logfile.txt
docker ps >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/logfile.txt

docker run -d -p 9001:5000 phase1_docker:latest >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/logfile.txt

docker ps >> /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/logfile.txt