import sys
import math

# parsing
X = [tuple(line.strip().split()) for line in open(sys.argv[1], 'r')]

# part 1
ans1 = sum(int(base) for val,base in X)
print(ans1)

# part 2
ans2 = sum(int(val, int(base)) for val,base in X)
print(ans2)

# part 3
B = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#'
q = ans2
pwr = math.floor( math.log(q, 65) )
ans3 = ''
while q:
    mul = q // (65 ** pwr)
    dig = B[mul]
    ans3 += dig
    q -= mul * (65 ** pwr)
    pwr -= 1
print(ans3)

