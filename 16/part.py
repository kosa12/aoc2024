with open("input.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]

n_rows = len(grid)
n_cols = len(grid[0])

def find_tile(c):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == c:
                return i, j

def adj4(i, j):
    adj = []
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if i + di in range(n_rows) and j + dj in range(n_cols) and grid[i + di][j + dj] != '#':
            adj.append((i + di, j + dj, (di, dj)))
    return adj

starti, startj = find_tile('S')
endi, endj = find_tile('E')

def pop_min(Q):
    minimum = min(Q, key=lambda x: x[0])
    Q.remove(minimum)
    return minimum

start_dir = (0, 1)
Q = [(0, (starti, startj, start_dir))]
dist = {}
dist[(starti, startj, start_dir)] = 0
prev = {}
prev[(starti, startj, start_dir)] = None

while len(Q) != 0:
    score, (ci, cj, dir) = pop_min(Q)

    for ni, nj, (di, dj) in adj4(ci, cj):
        alt = score + 1
        if dir != (di, dj):
            alt += 1000
        new_node = (ni, nj, (di, dj))
        if new_node not in dist or alt < dist[new_node]:
            dist[new_node] = alt
            prev[new_node] = (ci, cj, dir)
            Q.append((alt, new_node))

min_score = float('inf')
end_node = None

for x in dist.keys():
    i, j, dir = x
    if i == endi and j == endj and dist[x] < min_score:
        min_score = dist[x]
        end_node = x

path = []
current = end_node
while current:
    path.append(current)
    current = prev[current]

path.reverse()

print(f"Minimum score: {min_score}")
