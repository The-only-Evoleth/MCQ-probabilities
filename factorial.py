def factorial(num):
    num = abs(round(num))
    if num>0:
        for i in range(1, num):
            num *= i
        return num
    elif num == 0:
        return 1