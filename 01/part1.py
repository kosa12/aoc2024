list1 = []
list2 = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        a, b = line.rstrip().split()
        list1.append(int(a))
        list2.append(int(b))

list1 = sorted(list1)
list2 = sorted(list2)

differences = [abs(a - b) for a, b in zip(list1, list2)]

solution = sum(differences)

print(solution)