def factorial( num):
    if num <= 0:
        return 1
    return num * factorial(num - 1)

number = 5
print(factorial(number))