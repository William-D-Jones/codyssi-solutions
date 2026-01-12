import sys

# parsing
X = [line.strip() for line in open(sys.argv[1], 'r')]
S = []
for i,x in enumerate(X):
    if x=='TRUE':
        out = True
    elif x=='FALSE':
        out = False
    else:
        assert False
    S.append( (i+1, out) )

# part 1
ans1 = sum(i for i,out in S if out)
print(ans1)

# part 2
ans2 = 0
for i in range(len(S)//2):
    if i % 2 == 0:
        ans2 += 1 if S[2*i][1] and S[2*i+1][1] else 0
    else:
        ans2 += 1 if S[2*i][1] or S[2*i+1][1] else 0
print(ans2)

# part 3
ans3 = 0
Lyr = [out for i,out in S]
while Lyr:
    ans3 += sum(1 for out in Lyr if out)
    Lyr_Next = []
    for i in range(len(Lyr)//2):
        if i % 2 == 0:
            Lyr_Next.append( Lyr[2*i] and Lyr[2*i+1] )
        else:
            Lyr_Next.append( Lyr[2*i] or Lyr[2*i+1] )
    Lyr = Lyr_Next
print(ans3)

