#!/bin/sh


FILE='08_linklist.txt'

python3 main.py -s 1 -d 1 -a 10 -t 1000 -f $FILE -v
python3 main.py -s 1 -d 100 -a 10 -t 1000 -f $FILE -v
python3 main.py -s 1 -d 1000 -a 10 -t 1000 -f $FILE -v
