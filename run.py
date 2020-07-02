#!/usr/bin/env python3

import argparse
import logging
import sys
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


# class RandomWalker:
#     def __init__(self, src):
#         self.pos = src
#         self.path = []
#         self.path.append(src)

#     def get_neighbors(self):
#         neighbors = list(g.neighbors(self.pos))
#         return neighbors

#     def move(self):
#         neighbors = self.get_neighbors()
#         dst = random.choice(neighbors)
#         self.pos = dst
#         self.path.append(dst)

args = parse_args()
src = args.src
dst = args.dst
agents = args.agents
trials = args.trials
filename = args.file
args.verbose

if args.verbose:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(message)s')

logging.debug(f'src: {src}')
logging.debug(f'dst: {dst}')
logging.debug(f'agents: {agents}')
logging.debug(f'traials: {trials}')
logging.debug(f'filename: {filename}')

# g = nx.Graph()
# with open(filename, 'r') as f:
#     for line in f:
#         i, j = map(int, line.split())
#         g.add_edge(i, j)
# n = len(g.nodes)

# error handling
# if

# sys.exit(1)

# first_meeting_time = []
# for _ in range(trials):
#     rw = RandomWalker(src)
#     cnt = 0
#     while rw.pos != dst:
#         rw.move()
#         cnt += 1
#     first_meeting_time.append(cnt)
#     print(cnt, rw.path)

# mu = sum(first_meeting_time) / len(first_meeting_time)

# print(mu)
