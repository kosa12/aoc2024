import re

total = 0
with open("input.txt", "r", encoding="utf-8") as file:
    line = file.read().replace("\n", "")
    expressions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    total += sum(int(x) * int(y) for x, y in expressions)

print(total)