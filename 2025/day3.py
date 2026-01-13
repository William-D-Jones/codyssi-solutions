import sys

# parsing
X = [line.strip().split() for line in open(sys.argv[1], 'r')]
Box = []
for x0,x1 in X:
    r0 = tuple(map(int,x0.split('-')))
    r1 = tuple(map(int,x1.split('-')))
    Box.append( (r0,r1) )

# part 1
ans1 = 0
for (b00,b01),(b10,b11) in Box:
    ans1 += b01-b00+1 + b11-b10+1
print(ans1)
    
# part 2
ans2 = 0
for (b00,b01),(b10,b11) in Box:
    ans2 += len(set(range(b00,b01+1)) | set(range(b10,b11+1)))
print(ans2)

# part 3
ans3 = 0
for i in range(len(Box)-1):
    (bi00,bi01),(bi10,bi11) = Box[i]
    (bj00,bj01),(bj10,bj11) = Box[i+1]
    uni = len(set(range(bi00,bi01+1)) | set(range(bi10,bi11+1)) | \
    set(range(bj00,bj01+1)) | set(range(bj10,bj11+1)))
    ans3 = max(ans3, uni)
print(ans3)

