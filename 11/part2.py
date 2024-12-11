import os

file = open('input.txt', 'r').read()

nums_str = file.split(' ')
nums = [int(n) for n in nums_str]

cache = {}
result = 0

def calc(x,n):
    if n == 0:
        return 1
    if (x, n) not in cache:
        if x == 0:
            result = calc(1, n - 1)
        elif len(str(x)) % 2 == 0:
            s = str(x)
            l = s[:len(s)//2]
            r = s[len(s)//2:]
            result = 0
            result += calc(int(l), n - 1)
            result += calc(int(r), n - 1)
        else:
            result = calc(x * 2024, n - 1)
        cache[(x, n )] = result
    return cache[(x, n)]

res = 0
for x in nums:
    res += calc(x, 75)
print(res)



