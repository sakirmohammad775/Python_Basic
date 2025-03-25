def full_name(first,last ,**addition):
    name=f'{first}{last}'
    for key,value in addition.items():
        print(key,value)
    return name

def a_lot(num1,num2):
    sum=num1+num2
    mullt=num1*num2
    remain=num1-num2
    return [sum,mullt,remain]
everything=a_lot(20,9)
print(everything)