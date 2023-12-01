import numpy as np
import functools
from collections import Counter, deque, defaultdict
import re

def get_input():
    with open('input', 'r') as file:
        contents = file.readlines()

    rates = {}
    edges = {}
    for line in contents:
        _, valve, _, _, rate, _, _, _, _, valves = line.split(' ', 9)
        rates[valve] = int(re.findall(r'\d+', rate)[0])
        edges[valve] = valves.strip().split(', ')

    return rates, edges


def main():
    rates, edges = get_input()

    @functools.cache
    def dfs(valve, time, visited):
        if time <= 1:
            return 0
        res = 0
        for other in edges[valve]:
            res = max(res, dfs(other, time-1, visited))
        if valve not in visited and rates[valve] > 0:
            visited = tuple(sorted([*visited, valve]))
            res = max(res, dfs(valve, time-1, visited) + rates[valve] * (time-1))
        return res

    print(dfs('AA', 30, ()))


def p2():
    rates, edges = get_input()
    fw = defaultdict(dict)
    for i in edges:
        for j in edges:
            if i == j:
                fw[i][j] = 0
            elif j in edges[i]:
                fw[i][j] = 1
            else:
                fw[i][j] = np.inf

    for i in edges:
        for j in edges:
            if i == j:
                continue
            for k in edges:
                if k == i or k == j:
                    continue
                fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

    # distances = defaultdict(dict)
    # for i in edges:
    #     for j in edges:
    #         if fw[i][j] < np.inf and rates[j] > 0:
    #             distances[i][j] = fw[i][j]

    valves = {valve: rate for valve, rate in rates.items() if rate > 0}

    @functools.cache
    def dfs(p1, p2, visited):
        res = 0
        for v, r in valves.items():
            if v in visited:
                continue
            nvisited = tuple(sorted([*visited, v]))

            v1, t1 = p1
            if v in fw[v1] and (t := t1 - fw[v1][v]) >= 1:
                t -= 1
                res = max(res, dfs((v, t), p2, nvisited) + t * r)
            v2, t2 = p2
            if v in fw[v2] and (t := t2 - fw[v2][v]) >= 1:
                t -= 1
                res = max(res, dfs(p1, (v, t), nvisited) + t * r)

        return res
    
    print(dfs(('AA', 26),('AA', 26),()))


if __name__ == '__main__':
    p2()
