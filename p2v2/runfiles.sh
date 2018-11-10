#!/usr/bin/env bash

echo 6
python broker.py 5000 &
wait
python publisher.py 7005 &
wait
python subscriber.py 6005 &
wait
echo 10
