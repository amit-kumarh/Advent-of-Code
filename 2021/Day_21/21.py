import itertools
die_list = list(range(1, 101))
die = itertools.cycle(die_list)

step = 0
pos1 = 6
pos2 = 4
player1 = 0
player2 = 0
while True:
    step += 3
    roll1 = next(die) + next(die) + next(die)
    pos1 = (pos1 + roll1) % 10
    if pos1 == 0:
        pos1 = 10
    player1 += pos1
    if player1 >= 21:
        break

    step += 3
    roll2 = next(die) + next(die) + next(die)
    pos2 = (pos2 + roll2) % 10
    if pos2 == 0:
        pos2 = 10
    player2 += pos2
    if player2 >= 21:
        break

print(step * player2)

## PART 2

games = {}
p1, p2, s1, s2, = [6, 4, 0, 0]

def play(p1, p2, s1, s2):
    global games
    if s2 >= 21:
        return (0, 1)
    if s1 >= 21:
        return (1, 0)
    
    if (p1, p2, s1, s2) in games:
        return games[(p1, p2, s1, s2)]
    
    cnt = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                np1 = (p1 + d1 + d2 + d3) % 10
                if np1 == 0:
                    np1 = 10
                ns1 = s1 + np1

                count1, count2, = play(p2, np1, s2, ns1)
                cnt = (cnt[0] + count2, cnt[1] + count1)
    
    games[(p1, p2, s1, s2)] = cnt
    return cnt

print(play(p1, p2, s1, s2))




                

