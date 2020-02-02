def solution(n):
    # D(n) = D(n-1) + D(n-2)
    sols = [0] * 1001
    sols[1] = 1
    sols[2] = 2

    for i in range(3, n+1):
        sols[i] = sols[i-1] + sols[i-2]

    return sols[n]


if __name__ == '__main__':
    n = int(input())
    print(solution(n) % 10007)
