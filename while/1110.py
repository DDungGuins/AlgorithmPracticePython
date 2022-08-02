N = int(input())
if (N < 10):
    N = N * 10
X = N
index = 0
while True:
    index = index + 1
    a, b = divmod(N, 10)
    M = a + b
    N = b * 10 + M % 10
    if X == N: break
print(index)

# good day sungmander..
