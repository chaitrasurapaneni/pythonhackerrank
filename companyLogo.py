from itertools import groupby


str = "adnfasmde"

ls = list(str.lower())
ls.sort()
sortedStr = "".join(ls)


mappedItems = ([ (key, len(list(value))) for key, value in groupby (ls, lambda x:x)])
mappedItems.sort(key=lambda x:x[1], reverse=True)

for x in range(3):
    item = mappedItems[x]
    print(*item)


