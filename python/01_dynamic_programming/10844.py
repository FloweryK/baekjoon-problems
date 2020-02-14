def solution(n):
    sols = [[0]*10 for _ in range(101)]
    sols[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    sols[2] = [0, 2, 2, 2, 2, 2, 2, 2, 2, 1]

    for i in range(3, n+1):
        sols[i][0] = 0
        sols[i][1] = sols[i-1][2] + sols[i-2][1]
        sols[i][2] = sols[i-1][1] + sols[i-1][3]
        sols[i][3] = sols[i-1][2] + sols[i-1][4]
        sols[i][4] = sols[i-1][3] + sols[i-1][5]
        sols[i][5] = sols[i-1][4] + sols[i-1][6]
        sols[i][6] = sols[i-1][5] + sols[i-1][7]
        sols[i][7] = sols[i-1][6] + sols[i-1][8]
        sols[i][8] = sols[i-1][7] + sols[i-1][9]
        sols[i][9] = sols[i-1][8]

    return sum(sols[n])


n = int(input())
print(solution(n) % 1000000000)

