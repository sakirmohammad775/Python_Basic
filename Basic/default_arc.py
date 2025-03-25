def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for i in numbers:
        sum = sum + i
        print(sum)
    return sum


total = all_sum(2, 4, 5, 6, 4)
print('all_sum',total)
