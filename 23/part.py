lines = open("input.txt", "r").read().splitlines()
puterMap = {}
for line in lines:
    
    puter1 = line.split("-")[0]
    puter2 = line.split("-")[1]
    if puter1 not in puterMap:
        puterMap[puter1] = set()
    if puter2 not in puterMap:
        puterMap[puter2] = set()
    puterMap[puter1].add(puter2)
    puterMap[puter2].add(puter1)
triplets = set()
for a in puterMap:
    am = puterMap[a]
    
    for b in am:
        bm = puterMap[b]
        for c in am.intersection(bm):
            if any(i[0] == "t" for i in [a, b, c]):
                triplet = frozenset({a, b, c})
                triplets.add(triplet)
print(len(triplets))