def max_opr(n, arr):
    count = 0
    while all(a % 2 == 0 for a in arr):
        arr = [a // 2 for a in arr]  
        count += 1
    return count

N = int(input())
arr = list(map(int, input().split()))
print(max_opr(N, arr))
