def factorial(num):
    total = 1
    while num > 1:
       total, num = total * num, num - 1    
    return total
    
number = 900
print(factorial(number))