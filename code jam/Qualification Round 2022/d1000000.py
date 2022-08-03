N = int(input())

for i in range(N):
    n = 1
    M = int(input())
    L = list(map(int, input().split()))
    L.sort()
    L.reverse()

    while L:
        if (L[-1]) >= n : n += 1
        L.pop()
    print("Case #%d: %d" %(i+1,n-1))
