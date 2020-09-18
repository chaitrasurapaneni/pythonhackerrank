items = [('ak', 1), ('aa', 1), ('ka', 2), ('ts', 2), ('sc', 2), ('as', 3), ('sa', 3),  ('ab', 3), ('va', 3)]
ranksDict = {}
for item in items:
    name = item[0]
    rank = item[1]
    ranksDict.setdefault(rank, 0)
    ranksDict[rank] += 1

print(ranksDict)

