def run():
    # D(n) = steps[n] + max(steps[n-1] + D(n-3), D(n-2))

    step = [0] * 300
    solution = [0] * 300

    T = int(input())

    for i in range(T):
        step[i] = int(input())

    solution[0] = step[0]
    solution[1] = step[0] + step[1]
    solution[2] = max(step[2] + step[1], step[2] + step[0])

    for i in range(3, T):
        solution[i] = step[i] + max(step[i-1] + solution[i-3], solution[i-2])

    print(solution[T-1])


if __name__ == '__main__':
    run()