def solution(n):
    # D(n) = D(n-2) + D(n-1) + ... + D(1) + 1
    # D(1) = 1
    # D(2) = 1

    sols = [0] * 91
    sols[1] = 1
    sols[2] = 1

    for i in range(3, n+1):
        sols[i] = sum(sols[1:i-1]) + 1

    return sols[n]


N = int(input())
print(solution(N))
