import sys

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
Num = list(map(int, X[:-1]))
Sign = X[-1]
assert len(Num)==len(Sign)+1

# part 1
ans1 = Num[0]
for mag,sign in zip(Num[1:],Sign):
    if sign=='+':
        ans1 += mag
    elif sign=='-':
        ans1 -= mag
    else:
        assert False
print(ans1)

# part 2
ans2 = Num[0]
for mag,sign in zip(Num[1:],Sign[::-1]):
    if sign=='+':
        ans2 += mag
    elif sign=='-':
        ans2 -= mag
    else:
        assert False
print(ans2)

# part 3
ans3 = int(str(Num[0])+str(Num[1]))
Num3 = [int(str(Num[2*i])+str(Num[2*i+1])) for i in range(len(Num)//2)]
for mag,sign in zip(Num3[1:],Sign[::-1]):
    if sign=='+':
        ans3 += mag
    elif sign=='-':
        ans3 -= mag
    else:
        assert False
print(ans3)

