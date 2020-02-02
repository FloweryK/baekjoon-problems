def solution(numbers, n):
    

n = int(input())
numbers = [0] * 100001
numbers[1:n+1] = [int(i) for i in input().split()]

