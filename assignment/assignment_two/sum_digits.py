def sum_digits(number):
    num1 = number // 1000
    num2 = (number - (number // 1000) * 1000) // 100
    num3 = (number - (number // 100) * 100) // 10
    num4 = (number - (number // 10) * 10)

    total = num1 + num2 + num3 + num4
    print(total)
    return total
