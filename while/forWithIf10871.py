N,X = map(int, input().split())

list=list(map(int, input().split()))
for i in range(N):
    a = list[i]
    if a<X:
        print(a, end=" ")
