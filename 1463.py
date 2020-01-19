# ref: https://www.acmicpc.net/problem/1463
# bottom-up (loop)


def solution(n):
    sol = [0] * (n + 1)

    for i in range(2, n+1):
        sol[i] = sol[i-1] + 1

        if i % 2 == 0:
            sol[i] = min(sol[i], sol[int(i/2)] + 1)
        if i % 3 == 0:
            sol[i] = min(sol[i], sol[int(i/3)] + 1)

    return sol[n]


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
