def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line=line.strip().split()
            for i in range(len(line)):
                line[i] = int(line[i])
            data.append(line)
    return data

def validate(level):
    increase = all(i > j for i, j in zip(level, level[1:]))
    decrease = all(i < j for i, j in zip(level, level[1:]))
    increment = all(abs(i - j) <= 3 for i, j in zip(level, level[1:]))
    return (increase or decrease) and increment

def repair(level):
    for i in range(len(level)):
        tmp = level[:]
        tmp.pop(i)
        if validate(tmp):
            return True
    return False

def part1(data):
    answer = 0
    for line in data:
        if validate(line):
            answer += 1
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    for line in data:
        if validate(line):
            answer += 1
        else:
            if repair(line):
                answer += 1
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)