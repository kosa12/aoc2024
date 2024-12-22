from operator import xor
from pathlib import Path


def mix(a, b):
    return xor(a, b)


def prune(a):
    return a % 16777216


def next_secret(x):
    x = prune(mix(x, x * 64))
    x = prune(mix(x, x // 32))
    x = prune(mix(x, x * 2048))

    return x


def get_idx(seed, idx):
    x = seed

    for _ in range(idx):
        x = next_secret(x)

    return x


def main():
    input_file = Path('input.txt')
    with input_file.open() as fin:
        lines = list(map(int, fin.read().strip().split('\n')))

    results = [get_idx(x, 2000) for x in lines]
    total_sum = sum(results)
    print('2000th secret numbers:', results)
    print('Sum of 2000th secret numbers:', total_sum)


if __name__ == '__main__':
    main()