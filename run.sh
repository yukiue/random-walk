#!/bin/sh -v
N=1000
FILE='08_linklist.txt'

echo "dst degree mu" > result-degree.txt
for b in `seq 2 $N`
do
    echo -n "$b "
    python3 main.py -s 1 -d $b -a 3 -t 1000 -f $FILE -v | awk '{print $NF}' | awk 'NR== 4;NR==8' | tr '\n' ' ' | sed 's/\s*$//' | sed 's/$/ \n/'
done >> result-degree.txt

echo "agents mu" > result-agents.txt
for a in `seq 1 100`
do
    echo -n "$a "
    python3 main.py -s 1 -d 2 -a $a -t 1000 -f $FILE -v | awk '{print $NF}' | awk 'NR==8' | tr '\n' ' ' | sed 's/\s*$//' | sed 's/$/ \n/'
done >> result-agents.txt
