n, x = map(int, input().split())
A = list(map(int, input().split()))

result = ''
for a in A:
    if a < x:
        result += str(a) + ' '
result = result[:-1]

print(result)