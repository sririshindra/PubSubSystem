#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("entered line 3 in startup")
import os, sys
# os.system("sh runfiles.sh")
from threading import Thread


def startbroker():
    os.system("python broker.py 5000")


t1 = Thread(target=startbroker)
t1.setDaemon(True)
t1.start()


def startsubscriber1():
    os.system("python subscriber.py 6000")


s0 = Thread(target=startsubscriber1)
s0.setDaemon(True)
s0.start()


def startsubscriber2():
    os.system("python subscriber.py 6001")

s1 = Thread(target=startsubscriber2)
s1.setDaemon(True)
s1.start()


def startsubscriber3():
    os.system("python subscriber.py 6002")


s2 = Thread(target=startsubscriber3)
s2.setDaemon(True)
s2.start()


def startsubscriber4():
    os.system("python subscriber.py 6003")


s3 = Thread(target=startsubscriber4)
s3.setDaemon(True)
s3.start()


def startsubscriber5():
    os.system("python subscriber.py 6004")

s4 = Thread(target=startsubscriber5)
s4.setDaemon(True)
s4.start()



def startpublisher1():
    os.system("python publisher.py 7000")


p0 = Thread(target=startpublisher1)
p0.setDaemon(True)
p0.start()


def startpublisher2():
    os.system("python publisher.py 7001")


p1 = Thread(target=startpublisher2)
p1.setDaemon(True)
p1.start()

def startpublisher3():
    os.system("python publisher.py 7002")


p2= Thread(target=startpublisher3)
p2.setDaemon(True)
p2.start()

def startpublisher4():
    os.system("python publisher.py 7003")


p3 = Thread(target=startpublisher4)
p3.setDaemon(True)
p3.start()

def startpublisher5():
    os.system("python publisher.py 7004")


p4 = Thread(target=startpublisher5)
p4.setDaemon(True)
p4.start()


while True:
    pass
