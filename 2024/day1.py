import sys

# parsing
X = [int(line) for line in open(sys.argv[1], 'r')]

# part 1
ans1 = sum(X)
print(ans1)

# part 2
ans2 = sum(sorted(X)[:-20])
print(ans2)

# part 3
ans3 = 0
for i,x in enumerate(X):
    if i % 2 == 0:
        ans3 += x
    else:
        ans3 -= x
print(ans3)

