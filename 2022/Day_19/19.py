import numpy as np
import functools
from collections import Counter, deque, defaultdict
import re
from dataclasses import dataclass, replace, astuple
from functools import cache

@dataclass
class State:
    ore: int
    clay: int
    obsidian: int
    geodes: int

    ore_bots: int
    clay_bots: int
    obsidian_bots: int
    geodes_bots: int

    time: int

def get_input():
    with open('ex', 'r') as file:
        contents = file.read().strip().split('\n')
        blueprints = [[int(x) for x in re.findall(r'\d+', line)] for line in contents]
        
    return blueprints


def geodes(bp):
    ore_cost, clay_cost, obs_cost, geode_cost = bp[1], bp[2], (bp[3], bp[4]), (bp[5], bp[6])
#   ore       ore        ore,clay  ore,obs
    state = State(0, 0, 0, 0, 1, 0, 0, 0, 24)
    max_ore = max(ore_cost, clay_cost, obs_cost[0], geode_cost[0])
    max_clay = obs_cost[1]
    max_obs = geode_cost[1]


    @cache
    def dfs(state):
        state = State(*state)
        if state.time == 0:
            return state.geodes
        
        state.ore += state.ore_bots
        state.clay += state.clay_bots
        state.obsidian += state.obsidian_bots
        state.geodes += state.geodes_bots

        state.ore = min(state.ore, max_ore * (24-state.time))
        state.clay = min(state.clay, max_clay * (24-state.time))
        state.obsidian = min(state.obsidian, max_obs * (24-state.time))

        score = 0
        if state.ore >= ore_cost and state.ore_bots < max_ore:
            new_state = replace(state)
            new_state.ore -= ore_cost
            new_state.ore_bots += 1
            new_state.time -= 1
            score = max(score, dfs(astuple(new_state)))
        if state.ore >= clay_cost and state.clay_bots < max_clay:
            new_state = replace(state)
            new_state.ore -= clay_cost
            new_state.clay_bots += 1
            new_state.time -= 1
            score = max(score, dfs(astuple(new_state)))
        if all(x >= y for x, y in zip((state.ore, state.clay), obs_cost)) and state.obsidian_bots < max_obs:
            new_state = replace(state)
            new_state.ore -= obs_cost[0]
            new_state.clay -= obs_cost[1]
            new_state.obsidian_bots += 1
            new_state.time -= 1
            score = max(score, dfs(astuple(new_state)))
        if all(x >= y for x, y in zip((state.ore, state.obsidian), geode_cost)):
            new_state = replace(state)
            new_state.ore -= geode_cost[0]
            new_state.obsidian -= geode_cost[1]
            new_state.geodes_bots += 1
            new_state.time -= 1
            score = max(score, dfs(astuple(new_state)))
        
        new_state = replace(state)
        new_state.time -= 1
        score = max(score, dfs(astuple(new_state)))

        return score

    return dfs(astuple(state))
            
def p1():
    blueprints = get_input()
    print(blueprints)
    ans = 0
    for bp in blueprints:
        score = geodes(bp)
        ans += score * bp[0]
    print(ans)

if __name__ == '__main__':
    p1()

