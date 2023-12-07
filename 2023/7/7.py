import sys
import collections
import functools

PART1 = False

with open(sys.argv[1]) as f:
    c = f.read().strip().splitlines()

def poker(h):
    cnt = collections.Counter(h)
    dist = sorted(list(x[1] for x in cnt.most_common()))
    if dist == [5]:
        return 0
    if dist == [1, 4]:
        return 1
    if dist == [2, 3]:
        return 2
    if dist == [1, 1, 3]:
        return 3
    if dist == [1, 2, 2]:
        return 4
    if dist == [1, 1, 1, 2]:
        return 5
    if dist == [1, 1, 1, 1, 1]:
        return 6

def solve(part1):
    CARDS = list('AKQJT98765432') if part1 else 'AKQT98765432J'
    bids = {}
    hands = {}
    for line in c:
        hand, bid = line.split()
        bids[hand] = int(bid)
        cnt = collections.Counter(hand)

        if part1:
            hands[hand] = poker(hand)
            continue

        if hand == 'JJJJJ':
            hands[hand] = 0
        else:
            common_num = max(cnt[x] for x in cnt if x != 'J')
            all = [x for x in cnt if cnt[x] == common_num and x != 'J']
            replacer = max(all, key=lambda x: CARDS.index(x))
            newhand = hand.replace('J', replacer)
            hands[hand] = poker(newhand) 

    def cmp(a, b):
        if hands[a] != hands[b]:
            if hands[a] > hands[b]:
                return -1
            else:
                return 1
        else:
            for i, j in zip(a, b):
                if i != j:
                    if CARDS.index(i) > CARDS.index(j):
                        return -1
                    else:
                        return 1

    res = sorted(list(hands.keys()), key=functools.cmp_to_key(cmp))
    ans = 0
    for i, r in enumerate(res):
        ans += bids[r] * (i+1)

    print(ans)

solve(True)
solve(False)
