import re

total = 0
with open("input.txt", "r", encoding="utf-8") as file:
    line = file.read().replace("\n", "")
    blocks = line.split("do()")
    for block in blocks:
        do = block.split("don't()")[0]
        expressions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", do)
        total += sum(int(x) * int(y) for x, y in expressions)

print(total)