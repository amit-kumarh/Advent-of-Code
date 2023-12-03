from collections import Counter, deque, defaultdict
import re
from typing import NamedTuple


class State(NamedTuple):
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
    with open("input", "r") as file:
        contents = file.read().strip().split("\n")
        blueprints = [[int(x) for x in re.findall(r"\d+", line)] for line in contents]

    return blueprints


def geodes(bp):
    ore_cost, clay_cost, obs_cost, geode_cost = (
        bp[1],
        bp[2],
        (bp[3], bp[4]),
        (bp[5], bp[6]),
    )
    init_state = State(0, 0, 0, 0, 1, 0, 0, 0, 32)
    max_ore = max(ore_cost, clay_cost, obs_cost[0], geode_cost[0])
    max_clay = obs_cost[1]
    max_obs = geode_cost[1]

    q = deque()
    q.append(init_state)
    seen = set()

    max_geodes = 0

    while q:
        state = State(*q.popleft())
        max_geodes = max(max_geodes, state.geodes)

        ore, clay, obsidian, geodes, ore_bots, clay_bots, obsidian_bots, geodes_bots, time = state
        if time == 0: continue

        ore = min(ore, max_ore * (time))
        clay = min(clay, max_clay * (time))
        obsidian = min(obsidian, max_obs * (time))

        state = State(ore + ore_bots, clay+ clay_bots, obsidian+obsidian_bots, geodes+geodes_bots, ore_bots, clay_bots, obsidian_bots, geodes_bots, time - 1)
        if state in seen:
            continue
        seen.add(state)

        q.append(state)

        if ore >= ore_cost and ore_bots < max_ore:
            q.append(
                State(
                    ore - ore_cost + ore_bots,
                    clay + clay_bots,
                    obsidian + obsidian_bots,
                    geodes + geodes_bots,
                    ore_bots + 1,
                    clay_bots,
                    obsidian_bots,
                    geodes_bots,
                    time - 1,
                )
            )
        if ore >= clay_cost and clay_bots < max_clay:
            q.append(
                State(
                    ore - clay_cost + ore_bots,
                    clay + clay_bots,
                    obsidian + obsidian_bots,
                    geodes + geodes_bots,
                    ore_bots,
                    clay_bots + 1,
                    obsidian_bots,
                    geodes_bots,
                    time - 1,
                )
            )
        if (
            all(x >= y for x, y in zip((ore, clay), obs_cost))
            and obsidian_bots < max_obs
        ):
            q.append(
                State(
                    ore - obs_cost[0] + ore_bots,
                    clay - obs_cost[1] + clay_bots,
                    obsidian + obsidian_bots,
                    geodes + geodes_bots,
                    ore_bots,
                    clay_bots,
                    obsidian_bots + 1,
                    geodes_bots,
                    time - 1,
                )
            )
        if all(x >= y for x, y in zip((ore, obsidian), geode_cost)):
            q.append(
                State(
                    ore - geode_cost[0] + ore_bots,
                    clay + clay_bots,
                    obsidian - geode_cost[1] + obsidian_bots,
                    geodes + geodes_bots,
                    ore_bots,
                    clay_bots,
                    obsidian_bots,
                    geodes_bots + 1,
                    time - 1,
                )
            )

    return max_geodes


def p1():
    blueprints = get_input()
    ans = 0
    for bp in blueprints:
        score = geodes(bp)
        print(score)
        ans += score * bp[0]
    print(ans)

def p2():
    blueprints = get_input()
    ans = 1
    for i in range(3):
        score = geodes(blueprints[i])
        ans *= score
    print(ans)


if __name__ == "__main__":
    #p1()
    p2()
