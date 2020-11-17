n, m = map(int, input().split())

arr = input().split()[:n]

A = set(input().split()[:m])
B = set(input().split()[:m])

happyCount = sum(i in A for i in arr)
unhappyCount = sum(i in B for i in arr)
print (happyCount - unhappyCount)
# print(A.intersection())
# print(B.intersection(arr))
# print(len(A.intersection())-len(B))
# print (sum([(i in A) - (i in B) for A]))

#for i in arr:
#    print(i, " : ", int(i in A))

#print(sum(i in A) for i in arr)

#print (happyCount)
#print (unhappyCount)


# K,M = map(int, input().split())
# n = 1
# number = K,M + n
#
# print(number)




