#!/usr/bin/env python3

import sys

agents = []
a_d = {}
a_mu = {}

with open(sys.argv[1], 'r') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        sep = line.split()
        a = int(sep[0])
        d = int(sep[1])
        mu = float(sep[2])
        agents.append(a)
        a_d[a] = d
        a_mu[a] = mu

# print(a_d)
# print(a_mu)

dmin = min(a_d.values())
dmax = max(a_d.values())

res = {}
for i in range(dmin, dmax + 1):
    res[i] = []

for i in agents:
    res[a_d[i]].append(a_mu[i])

for d, mu in res.items():
    if len(mu) != 0:
        print(d, sum(mu) / len(mu))
    else:
        print(d, '0')
