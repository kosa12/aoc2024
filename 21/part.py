from collections import deque
from itertools import permutations

num_grid = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0', 'A']]
dir_grid = [['', '^', 'A'], ['<', 'v', '>']]
inputs = ['803A', '528A', '586A', '341A', '319A']


def bfs(i, j, target, grid, perm):
  queue = deque()
  queue.append((i, j, ''))
  visited = set()
  visited.add((i, j))
  while len(queue) > 0:
    i, j, path = queue.popleft()
    if grid[i][j] == target:
      return path
    for di, dj, s in perm:
      ni = i + di
      nj = j + dj
      if ni < 0 or nj < 0 or ni >= len(grid) or nj >= len(grid[0]):
        continue
      if grid[ni][nj] != '' and (ni, nj) not in visited:
        visited.add((ni, nj))
        queue.append((ni, nj, path + s))
  return -1


def calc(start_i, start_j, in_, grid, perm):
  si, sj = start_i, start_j
  path = ''
  for c in in_:
    path += bfs(si, sj, c, grid, perm)
    path += 'A'
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == c:
          si, sj = i, j
  return path


third = []
for in_ in inputs:
  path = '0' * 10**6
  for x in permutations([(0, -1, '<'), (-1, 0, '^'), (1, 0, 'v'), (0, 1, '>')]):
    p1 = calc(3, 2, in_, num_grid, x)
    p2 = calc(0, 2, p1, dir_grid, x)
    p3 = calc(0, 2, p2, dir_grid, x)
    if len(p3) < len(path):
      path = p3
  third.append(path)

res = 0
for in_, path in zip(inputs, third):
  print(in_, len(path))
  res += int(in_[:-1]) * len(path)
print(res)