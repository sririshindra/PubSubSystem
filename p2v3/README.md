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

cd ProjectFolder/p2v3  <br />
docker-compose build <br />
docker-compose up <br />


## Tests

Open terminal <br />
<b>Start the docker container with pub/sub system</b> <br />
cd ProjectFolder/p2v3/  <br />
docker-compose build <br />
docker-compose up <br />


<b> open the browser.</b> <br />
Open the browser on the url '0.0.0.0:6001' to get the subscriber <br />
Open the browser on the url '0.0.0.0:7000' in another tab  to get the publisher<br />


subscribe to one or more topics in the subscriber tab.  <br />
submit topic_name and message name in the publisher tab.


## Demo

To use the pub/sub application simply go to the localhost:5000/ url and enter the source and destination in the textboxes. 
 <br />
![picture](resources/images/subscriber.jpg)  <br />
![picture](resources/images/publisher.jpg)

## Credits
http://flask.pocoo.org<br />
https://www.python.org<br />
https://www.docker.com<br />


## License
MIT © [rishi, divya 2018]()