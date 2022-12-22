import numpy as np
import functools
from collections import Counter, deque
import re

def get_input():
    with open('input', 'r') as file:
        packets = file.read().strip().split('\n\n')
    packets = [[*map(eval, packet.split('\n'))] for packet in packets]
    return packets
    

def compare(a, b):
    match a, b:
        case int(), int():
            return a-b
        case list(), int():
            return compare(a, [b])
        case int(), list():
            return compare([a], b)
        case list(), list():
            for res in map(compare, a, b):
                if res:
                    return res
            return len(a) - len(b)


def solve(part):
    packets = get_input()
    if part == 1:
        print(sum(i+1 for i, p in enumerate(packets) if compare(*p) < 0))
    else:
        packets = sum(packets, [[[2]], [[6]]])
        packets.sort(key=functools.cmp_to_key(compare))
        print((packets.index([[2]])+1) * (packets.index([[6]])+1))


if __name__ == '__main__':
    solve(1)
    solve(2)
