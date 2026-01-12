import sys
from collections import deque

# parsing
X = [tuple(line.strip().split(' <-> ')) for line in open(sys.argv[1], 'r')]
Path = {}
for src,tar in X:
    if src not in Path:
        Path[src] = []
    if tar not in Path:
        Path[tar] = []
    Path[src].append(tar)
    Path[tar].append(src)

# part 1
ans1 = len(Path)
print(ans1)

# part 2
s = 'STT'
step_max = 3
Q = deque([ (0, s) ])
Seen = {s}
while Q:
    step, pnt = Q.popleft()
    # check if the journey is complete
    if step >= step_max:
        continue
    step_next = step + 1
    for pnt_next in Path[pnt]:
        if pnt_next in Seen:
            continue
        Seen.add(pnt_next)
        Q.append( (step_next, pnt_next) )
ans2 = len(Seen)
print(ans2)

# part 3
s = 'STT'
Q = deque([ (0, s) ])
Seen = {s}
ans3 = 0
while Q:
    step, pnt = Q.popleft()
    step_next = step + 1
    for pnt_next in Path[pnt]:
        if pnt_next in Seen:
            continue
        Seen.add(pnt_next)
        ans3 += step_next
        Q.append( (step_next, pnt_next) )
print(ans3)

