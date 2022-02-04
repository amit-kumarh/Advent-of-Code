import re, copy
from collections import defaultdict, deque

GOALS = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
    2: 'A',
    4: 'B', 
    6: 'C',
    8: 'D'

}

WEIGHTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')

        board = ['.', '.', [], '.', [], '.', [], '.', [], '.', '.']
        for line in contents:
            letters = re.findall('#+([A-Z])#([A-Z])#([A-Z])#([A-Z])#+', line)
            if letters:
                for i, j in zip([2, 4, 6, 8], [0, 1, 2, 3]):
                    board[i].append(letters[0][j])

    return board

board = get_input()

def canReach(board, curr, dest):
    a = min(curr, dest)
    b = max(curr, dest)
    for pos in range(curr+1, dest):
        if pos == curr:
            continue
        if pos in GOALS:
            continue
        if board[pos] != '.':
            return False
    return True

def isValidRoom(board, room, letter):
    inroom = board[room]
    return len(inroom) == inroom.count(letter) + inroom.count('.')

def getTopLetter(room):
    for i in room:
        if i != '.':
            return i


def possibleMoves(board, curr):
    letters = board[curr]

    if curr not in GOALS: # if we've moved out of initial goal space, we can only move to our finishing goal
        goal = GOALS[letters]
        if canReach(board, curr, goal) and isValidRoom(board, goal, letters):
            return [goal] 
        return []

    letter = getTopLetter(letters)
    goal = GOALS[letter]
    if curr == GOALS[letter] and isValidRoom(board, goal, letter): # piece already solved
        return []
    

    possible = []
    for dest in range(len(board)):
        if curr == dest:
            continue
        if dest in GOALS: # can only move into goal if it's ours and there is nothing else in it.
            if dest != GOALS[letter]:
                continue
        if GOALS[letter] == dest and (not isValidRoom(board, goal, letter)):
            continue

        if canReach(board, curr, dest):
            possible.append(dest)
    
    return possible

def move(board, curr, dest):
    new_board = copy.deepcopy(board)
    letter = getTopLetter(board[curr])
    dist = abs(dest-curr)

    if len(new_board[curr]) == 1:
        new_board[curr] = '.'
    else:
        for idx, i in enumerate(new_board[curr]):
            dist += 1
            if i != '.':
                new_board[curr][idx] = '.'
                break
    
    if len(new_board[dest]) == 1:
        new_board[dest] = letter
    else:
        for idx, i in enumerate(new_board[dest]):
            dist += 1
            if i == '.':
                new_board[dest][idx] = letter
                break
    
    return new_board, dist * WEIGHTS[letter]

def toTuple(board):
    nboard = board[:]
    for i, j in enumerate(board):
        if isinstance(j, list):
            nboard[i] = tuple(j)

    return tuple(nboard)


def bfs(board):
    states = {toTuple(board): 0}
    queue = deque()
    queue.append(board)

    while queue:
        if len(queue) % 1000 == 0: print(len(queue))
        board = queue.popleft()

        for curr, letters in enumerate(board):
            if getTopLetter(letters) is None:
                continue

            dests = possibleMoves(board, curr)

            for dest in dests:
                nboard, addl_cost = move(board, curr, dest)
                tboard = toTuple(nboard)
                cost = states.get(tboard, 9999999)
                ncost = states[toTuple(board)] + addl_cost
                if ncost < cost:
                    states[tboard] = ncost
                    queue.append(nboard)
    
    return states

states = bfs(board)
p1 = states[('.', '.', ('A', 'A'), '.', ('B', 'B'), '.', ('C', 'C'), '.', ('D', 'D'), '.', '.')]
print(p1)


