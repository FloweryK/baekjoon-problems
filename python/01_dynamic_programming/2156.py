def solution(wine, n):
    # D(n) = max(D[n-1], wine[n]+D[n-2], wine[n]+wine[n-1]+D[n-3])
    D = [0 for _ in range(10000+1)]
    D[1] = wine[1]
    D[2] = wine[1] + wine[2]
    D[3] = max(wine[1]+wine[2], wine[1]+wine[3], wine[2]+wine[3])

    for i in range(4, n+1):
        D[i] = max(D[i-1], wine[i]+D[i-2], wine[i]+wine[i-1]+D[i-3])

    return D[n]


n = int(input())

wine = [0 for _ in range(10000+1)]
for i in range(1, n+1):
    wine[i] = int(input())

print(solution(wine, n))
