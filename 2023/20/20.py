import sys
import collections
from enum import Enum
from dataclasses import dataclass
from math import prod, lcm

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

class ModType(Enum):
    Ff = 0
    Con = 1
    Broadcast = 2

class Pulse(Enum):
    Lo = 1
    Hi = 2
    
@dataclass
class Module():
    type: ModType
    children: tuple
    memory: dict | bool| None
    name: str

    def get_key(self):
        return self.name + str(self.type) + str(self.children) + str(self.memory)


def get_mods():
    mods = {}
    for line in contents:
        source, children = line.split(' -> ')
        name = source if source[0] not in '%&' else source[1:]
        children = tuple(children.split(', '))
        match source[0]:
            case '%':
                mods[name] = Module(ModType.Ff, children, False, name)
            case '&':
                mods[name] = Module(ModType.Con, children, {}, name)
            case 'b':
                mods[name] = Module(ModType.Broadcast, children, None, name)
            case _: assert False

    for name, mod in mods.items():
        for c in mod.children:
            if c in mods:
                if mods[c].type == ModType.Con:
                    mods[c].memory[name] = Pulse.Lo
    return mods

pulses = {Pulse.Lo: 0, Pulse.Hi: 0}
state = get_mods()
broadcast = list(filter(lambda x: x.type == ModType.Broadcast, state.values()))[0]
los, cycles, i = {}, {}, 0

while True:
    i += 1
    q = collections.deque()
    pulses[Pulse.Lo] += 1
    for c in broadcast.children:
        q.append((c, Pulse.Lo, broadcast.name))

    while q:
        name, pulse, prev = q.popleft()

        # cycle detection - the components that make up rx are hardcoded from input
        if name in ['gc', 'sz', 'cm', 'xf'] and pulse == Pulse.Lo:
            if name in los:
                cycles[name] = i - los[name]
            else:
                los[name] = i
        if len(cycles) == 4:
            print(lcm(*cycles.values()))
            sys.exit()

        curr = state.get(name, None)
        pulses[pulse] += 1
        match (curr.type if curr else None):
            case ModType.Ff:
                if pulse == Pulse.Lo:
                    curr.memory = not curr.memory
                    for c in curr.children:
                        if curr.memory:
                            q.append((c, Pulse.Hi, name))
                        else:
                            q.append((c, Pulse.Lo, name))
                else:
                    continue
            case ModType.Con:
                curr.memory[prev] = pulse
                for c in curr.children:
                    if all(x == Pulse.Hi for x in curr.memory.values()):
                        q.append((c, Pulse.Lo, name))
                    else:
                        q.append((c, Pulse.Hi, name))

    if i == 1000:
        print(prod(pulses.values()))
