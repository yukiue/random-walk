#!/usr/bin/env python3

import argparse
import networkx as nx
import random


def parse_args():
    parser = argparse.ArgumentParser(
        description='calculate first meeting time')

    parser.add_argument('-s',
                        '--src',
                        help='source node id',
                        type=int,
                        default=1)
    parser.add_argument('-d',
                        '--dst',
                        help='destination node id',
                        type=int,
                        default=2)
    parser.add_argument('-a',
                        '--agents',
                        help='number of agents',
                        type=int,
                        default=1)
    parser.add_argument('-t',
                        '--trials',
                        help='number of trials',
                        type=int,
                        default=1)
    parser.add_argument('-f',
                        '--file',
                        help='input file name',
                        type=str,
                        default='list.txt')
    parser.add_argument('-v',
                        '--verbose',
                        help='verbose mode',
                        action='store_true')

    args = parser.parse_args()

    return args


class RandomWalker:
    def __init__(self, src):
        self.pos = src
        self.path = []
        self.path.append(src)

    def get_neighbors(self):
        neighbors = list(g.neighbors(self.pos))
        return neighbors

    def move(self):
        neighbors = self.get_neighbors()
        dst = random.choice(neighbors)
        self.pos = dst
        self.path.append(dst)


args = parse_args()
src = args.src
dst = args.dst
agents = args.agents
trials = args.trials
filename = args.file
verbose_mode = args.verbose

g = nx.Graph()
with open(filename, 'r') as f:
    for line in f:
        i, j = map(int, line.split())
        g.add_edge(i, j)
n = len(g.nodes)
first_meeting_time = []
for _ in range(trials):
    rw = {}
    visited_node = []
    cnt = 0
    for i in range(agents):
        rw[i] = RandomWalker(src)
    while dst not in visited_node:
        for i in range(agents):
            rw[i].move()
            visited_node.append(rw[i].pos)
            # print(f'node: {i}\tstep: {cnt}\tpath: {rws[i].path}')
        cnt += 1
    first_meeting_time.append(cnt)

if verbose_mode:
    print(f'number of nodes: {n}')
    print(f'source node id: {src}')
    print(f'destination node id: {dst}')
    print(f'number of agents: {agents}')
    print(f'number of traials: {trials}')
    print(f'filename: {filename}')
    print(f'degree of node {dst}: {g.degree(dst)}')

mu = sum(first_meeting_time) / len(first_meeting_time)
print(mu)

# first_meeting_time = []
# for _ in range(trials):
#     rw = RandomWalker(src)
#     cnt = 0
#     while rw.pos != dst:
#         rw.move()
#         cnt += 1
#     first_meeting_time.append(cnt)
#     # print(f'{cnt} {rw.path}')
