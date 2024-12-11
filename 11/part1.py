import os

file_path = os.path.join('./', 'input.txt')
file = open(file_path, 'r').read()

nums_str = file.split(' ')
nums = [int(n) for n in nums_str]

for _ in range(25):
    ans = []
    for i,n in enumerate(nums):
        if n == 0:
            ans.append(1)
        elif len(str(n)) % 2 == 0:
            s = str(n)
            l = s[:len(s)//2]
            r = s[len(s)//2:]
            ans.append(int(l))
            ans.append(int(r))
        else:
            ans.append(n * 2024)
    nums = ans
print(len(nums))