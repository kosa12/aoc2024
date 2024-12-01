list1 = []
list2 = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        a, b = line.rstrip().split()
        list1.append(int(a))
        list2.append(int(b))

list1 = [a * list2.count(a) for a in list1]

solution = sum(list1)

print(solution)