# Random Walk on Network

# Descriptions
usage: main.py [-h] [-s SRC] [-d DST] [-a AGENTS] [-t TRIALS] [-f FILE] [-v]

calculate first hitting time for random walks on network

optional arguments:
  -h, --help            show this help message and exit
  -s SRC, --src SRC     source node id
  -d DST, --dst DST     destination node id
  -a AGENTS, --agents AGENTS
                        number of agents
  -t TRIALS, --trials TRIALS
                        number of trials
  -f FILE, --file FILE  input file name
  -v, --verbose         verbose mode

# Examples
`./main.py -s 1 -d 2 -a 4 -t 100 -f list.txt`
```
average first hitting time: 123.13
```
`./main.py -s 1 -d 2 -a 4 -t 100 -f list.txt -v`
```
number of nodes: 100
source node id: 1
destination node id: 2
degree of destination node: 21
number of agents: 4
number of traials: 100
filename: list.txt
average first hitting time: 114.98
```
