## EMULATING PUB/SUB DISTRIBUTED SYSTEM USING DOCKER CONTAINERS
The purpose of the project is to implement the pub/sub system with publishers and subscribers. The publishers 
publish a message to a topic and the pub/sub system delivers said message to all the subscribers that are subscribed to 
a topic.

## Motivation
The motivation behind the project is to learn the following.
1) Building systems using Docker. <br />
2) Working with web interface to invoking Docker. <br />
3) Building a distributed pub/sub system. <br />

## Code style
PEP 8 for python

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Tech/framework used
<b>Technologies used</b>
- [python](http://python.org) <br />
- [flask](http://flask.pocoo.org) <br />
- [docker](https://www.docker.com) <br />

<b>Built with</b>
- [Intellij IDEA](https://www.jetbrains.com/idea/) <br />

## Installation and setup

Open terminal <br />

<b>Install the necessary python packages</b> <br />
pip install pymongo <br />
pip install flask <br />

<b>Install docker in your system </b> <br />
https://docs.docker.com/install/  <br />

cd ProjectFolder/p2v2  <br />
docker build -t p2v2:latest .  <br />
docker run -d  -p 5000:5000 -p 6005:6005 -p 7005:7005 -i p2v2:latest  <br />


## Tests

Open terminal <br />
<b>Start the docker container with pub/sub system</b> <br />
cd ProjectFolder/p2v2  <br />
docker run -d  -p 5000:5000 -p 6000-6010:6000-6010 -p 7000-7010:7000-7010 -i p2v2:latest <br />

<b> open the browser.</b> <br />
Open the browser on the urls '0.0.0.0:6001-6005' to get the subscribers <br />
Open the browser on the url '0.0.0.0:7001-7005' in another tab  to get the publishers<br />


subscribe to one or more topics in one or more subscriber tabs.  <br />
submit topic_name and message name in one or more publisher tabs.


## Demo

To use the pub/sub application simply go to the localhost:5000/ url and enter the source and destination in the textboxes. 
 <br />
![picture](resources/images/subscriber.jpg) <br />
![picture](resources/images/publisher.jpg)

## Credits
http://flask.pocoo.org<br />
https://www.python.org<br />
https://www.docker.com<br />


## License
MIT © [rishi, divya 2018]()