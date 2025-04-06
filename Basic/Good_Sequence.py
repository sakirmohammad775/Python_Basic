def good_sequence(n, arr):
    fre_count = {}
    for number in arr:
        fre_count[number] = fre_count.get(number, 0) + 1
    
    remove = 0
    for number, count in fre_count.items():
        if count > number:
            remove += count - number
        elif count < number:
            remove += count 
    
    return remove
n = int(input())
arr = list(map(int, input().split()))
print(good_sequence(n, arr))
