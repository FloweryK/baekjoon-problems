# D(n) = D(n-1) + D(n-2) + D(n-3)


def solution(n):
    if n < 3:
        memoization = [0] * 4
    else:
        memoization = [0] * (n+1)

    memoization[0] = 0
    memoization[1] = 1
    memoization[2] = 2
    memoization[3] = 4

    if n > 3:
        for j in range(4, n+1):
            memoization[j] = memoization[j-1] + memoization[j-2] + memoization[j-3]

    return memoization[n]


if __name__ == '__main__':
    T = int(input())
    test = []
    for i in range(T):
        test.append(int(input()))

    for t in test:
        print(solution(t))

