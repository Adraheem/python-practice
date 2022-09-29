def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


if __name__ == '__main__':
    number = int(input("Enter a number to check if it is perfect: "))
    if is_perfect(number):
        print("It is a perfect number")
    else:
        print("It is NOT a perfect number")
