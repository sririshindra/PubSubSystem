#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("enetered line 3 in startup")
import os, sys
# os.system("sh runfiles.sh")
from threading import Thread


def startbroker():
    os.system("python broker.py 5000")


def startsubscriber():
    os.system("python subscriber.py 6005")

t3 = Thread(target=startsubscriber)
t3.setDaemon(True)
t3.start()


t1 = Thread(target=startbroker)
t1.setDaemon(True)
t1.start()


def startpublisher():
    os.system("python publisher.py 7005")


t2 = Thread(target=startpublisher)
t2.setDaemon(True)
t2.start()







while True:
    pass
