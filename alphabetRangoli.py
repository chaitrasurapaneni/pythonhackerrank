import string

n = int(input())
alphaArr = list(string.ascii_lowercase)

for i in range(n-1, 0, -1):
   print(("-".join(alphaArr[i:n][::-1] + alphaArr[i + 1:n])).center(4 * n -3, "-"))

for i in range(n):
   print(("-".join(alphaArr[i:n][::-1] + alphaArr[i + 1:n])).center(4 * n -3, "-"))
# print(*range(0, n, 1))
# print(*range(n, 0, -1))




# --------e--------
# ------e-d-e-----
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------


