def solution(cost, n):
    # Red:   D[n][0] = cost[i][0] + min(D[n-1][1], D[n-1][2])
    # Green: D[n][1] = cost[i][1] + min(D[n-1][0], D[n-1][2])
    # Blue:  D[n][2] = cost[i][2] + min(D[n-1][0], D[n-1][1])

    sols = [[0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        sols[i][0] = cost[i][0] + min(sols[i-1][1], sols[i-1][2])
        sols[i][1] = cost[i][1] + min(sols[i-1][0], sols[i-1][2])
        sols[i][2] = cost[i][2] + min(sols[i-1][0], sols[i-1][1])

    return min(sols[n][0], sols[n][1], sols[n][2])


N = int(input())
cost = [[0, 0, 0] for _ in range(1001)]

for i in range(1, N+1):
    red, green, blue = input().split()
    cost[i][0] = int(red)
    cost[i][1] = int(green)
    cost[i][2] = int(blue)

print(solution(cost, N))
