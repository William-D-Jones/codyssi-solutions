import sys
import re

def calc(val, fun, op):
    if fun == 'ADD':
        return val + op
    elif fun == 'MULTIPLY':
        return val * op
    elif fun == 'RAISE TO THE POWER OF':
        return val ** op
    else:
        assert False

def get_price(Order, qual, Op):
    price = qual
    for nm in Order:
        fun, op = Op[nm]
        price = calc(price, fun, op)
    return price

# parsing
X0,X1 = open(sys.argv[1], 'r').read().strip().split('\n\n')
Op = {}
for x in X0.split('\n'):
    M = re.match(r'^Function ([A-Z]+): (.+) ([0-9]+)$', x)
    nm = M.group(1)
    fun = M.group(2)
    op = int(M.group(3))
    Op[nm] = (fun, op)
Qual = list(map(int, X1.split('\n')))

# part 1
if len(Qual) % 2 == 1:
    qual1 = sorted(Qual)[len(Qual)//2]
else:
    qual1 = (sorted(Qual)[len(Qual)//2-1] + sorted(Qual)[len(Qual)//2]) / 2
ans1 = get_price(['C', 'B', 'A'], qual1, Op)
print(ans1)

# part 2
qual2 = sum(qual for qual in Qual if qual % 2 == 0)
ans2 = get_price(['C', 'B', 'A'], qual2, Op)
print(ans2)

# part 3
max_price = 15000000000000
ans3 = 0
for qual in Qual:
    price = get_price(['C', 'B', 'A'], qual, Op)
    if qual > ans3 and price <= max_price:
        ans3 = qual
print(ans3)

