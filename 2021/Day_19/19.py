from collections import *
import copy
from itertools import combinations, permutations
from scipy.spatial.transform import rotation as R
import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n\n')

        final = []
        for i, sec in enumerate(contents):
            final.append([])
            lines = sec.split('\n')
            for line in lines[1:]:
                line = line.strip().split(',')
                final[i].append((int(line[0]), int(line[1]), int(line[2])))

    return final 

scanners = get_input()

def getRots(point):
    rots = []
    x,y,z = point
    for perm in permutations([x,y,z]):
        rots += (rot4(perm[0], perm[1], perm[2]))
    return rots
    

def rot4(x,y,z):
    rots = []
    for X in [-1, 1]:
        for Y in [-1, 1]:
            for Z in [-1, 1]:
                rots.append([X*x, Y*y, Z*z])
    return rots


def fingerprint(scanners):
    fingerprints = [] 
    for scanner in scanners:
        scanner_distances = []
        for b1 in scanner:
            distances = []
            hx, hy, hz = b1

            for b2 in scanner:
                if b1 == b2:
                    continue
                x,y,z = b2
                distances.append((hx-x)**2 + (hy-y)**2 + (hz-z)**2)

            scanner_distances.append(distances)
            
        fingerprints.append(scanner_distances)
    
    return fingerprints


def rotate(orig, idx, matches):
    global scanners
    for rot in range(48):
        test = [getRots(match[1]) for match in matches]        
        distances = []

        for i, point in enumerate(test):
            x1, y1, z1 = matches[i][0]
            x2, y2, z2 = point[rot]
            distances.append((x2+x1, y2+y1, z2+z1))
        

        if len(Counter(distances)) == 1:
            for i, point in enumerate(matches):
                x1, y1, z1 = point[0]
                x2, y2, z2 = test[i][rot]
                diff = [x2+x1, y2+y1, z2+z1]
                if 0 not in diff:
                    break
            
            print(diff)
            print(rot)

            rotbeacons = []
            for i, point in enumerate(scanners[idx]):
                point = getRots(point)[rot]
                point = [-1*(point[i]-diff[i]) for i in [0,1,2]]
                scanners[idx][i] = tuple(point)
            return diff



    
fingerprints = fingerprint(scanners)

#scanners = [scanners[0]]+ [scanners[1]] + [scanners[4]]

testrot = getRots([1, 2, 3])
print(len(testrot))

beacons = scanners[0]
known_scanners = [0]
scanner_locs = []

while True:
    fingerprints = fingerprint(scanners)
    for i in known_scanners:
        for j, test in enumerate(scanners):
            if j in known_scanners:
                continue
            counter = 0
            matches = []
            for b1i, b1 in enumerate(fingerprints[i]):
                for b2i, b2 in enumerate(fingerprints[j]):
                    if len(set(b1).intersection(set(b2))) >= 11:
                        counter += 1
                        matches.append((scanners[i][b1i], scanners[j][b2i]))
            
            if counter == 12:
                scanner_locs.append(rotate(i, j, matches))
                assert matches[0][1] not in scanners[j]
                known_scanners.append(j)
                beacons += scanners[j]
                break

    if len(known_scanners) == len(scanners):
        break
    
def manhattan(num, num2):
    x1, y1, z1 = num
    x2, y2, z2 = num2

    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

maxDist = 0
for i in scanner_locs:
    for j in scanner_locs:
        if i == j:
            continue
        dist = manhattan(i, j)
        if dist > maxDist:
            maxDist = dist

print(len(Counter(beacons)))
print(known_scanners)
print(maxDist)
