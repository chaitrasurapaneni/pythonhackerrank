from itertools import product

K,M = map(int,input().split())
# print("K = ", K)
# print("M = ", M)
N = list(map(int, input().split()[1:]) for _ in range(K))

prodN = list(product(*N))
# print("================")
# print(prodN)

def f1(array):
    return ( sum(x**2 for x in array)% M)

resultArray = list(map(f1, prodN))
print(max(resultArray))
# print ("result:")
# print (resultArray)
# print ("Max: ", max(resultArray))