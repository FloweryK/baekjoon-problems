def solution(tree, n):
    score = [[0] * 501 for _ in range(501)]

    for i in range(1, n+1):
        for j in range(1, i+1):
            score[i][j] = tree[i][j] + max(score[i-1][j-1], score[i-1][j])

    return max(score[n])


n = int(input())
tree = [[0]*501 for _ in range(501)]

for i in range(1, n+1):
    line = input().split()

    for j in range(1, len(line)+1):
        tree[i][j] = int(line[j-1])

print(solution(tree, n))

