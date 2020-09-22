from itertools import groupby
S = "1222311"
Sl = list(S)
print([(len(list(value)), key) for key, value in groupby(Sl, lambda x: int(x))])
