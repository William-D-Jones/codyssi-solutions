import sys

def merge_ranges(R):
    M = []
    for r0,r1 in R:
        pnt = 0
        while pnt<len(M):
            m0,m1 = M[pnt]
            if min(m1,r1)-max(m0,r0)>=0:
                r0,r1 = min(r0,m0),max(r1,m1)
                M.pop(pnt)
                pnt -= 1
            pnt += 1
        M.append( (r0,r1) )
    return M

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
for box in Box:
    M = merge_ranges(box)
    ans2 += sum(m1-m0+1 for m0,m1 in M)
print(ans2)

# part 3
ans3 = 0
for i in range(len(Box)-1):
    boxi = Box[i]
    boxj = Box[i+1]
    M = merge_ranges([*boxi, *boxj])
    tot = sum(m1-m0+1 for m0,m1 in M)
    ans3 = max(ans3, tot)
print(ans3)

