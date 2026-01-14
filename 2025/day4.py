import sys

A = ord('A')

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]

# part 1
ans1 = 0
for x in X:
    ans1 += sum(ord(char)-A+1 for char in x)
print(ans1)

# part 2
ans2 = 0
for x in X:
    end = len(x) // 10
    mid = len(x) - (2 * end)
    ans2 += \
    sum(ord(char)-A+1 for char in x[:end]) + \
    sum(ord(char)-A+1 for char in x[-end:]) + \
    sum(map(int,list(str(mid))))
print(ans2)

# part 3
ans3 = 0
for x in X:
    Q = list(x)
    n = 1
    char = Q.pop()
    tot = 0
    while Q:
        while Q and Q[-1] == char:
            n += 1
            Q.pop()
        tot += ord(char)-A+1 + sum(map(int,list(str(n))))
        if len(Q)==1:
            tot += ord(Q.pop())-A+1 + 1
        elif len(Q)>1:
            char = Q.pop()
            n = 1
    ans3 += tot
print(ans3)

