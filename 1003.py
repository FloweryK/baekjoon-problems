def solution(n):
    # D(n)[0] = D(n)[0] + D(n)[0]
    # D(n)[1] = D(n)[1] + D(n)[1]
    # D(0) = (1, 0)
    # D(1) = (0, 1)

    sols = [[0, 0] for _ in range(n+2)]
    sols[0] = [1, 0]
    sols[1] = [0, 1]

    for i in range(2, n+1):
        sols[i][0] = sols[i-1][0] + sols[i-2][0]
        sols[i][1] = sols[i-1][1] + sols[i-2][1]

    return sols[n]


def run():
    T = int(input())

    for i in range(T):
        n = int(input())
        sol = solution(n)
        print('%i %i' % (sol[0], sol[1]))


if __name__ == '__main__':
    run()