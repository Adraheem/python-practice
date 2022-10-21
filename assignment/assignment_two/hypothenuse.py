import math


def calculate_hypothenuse(num1, num2):
    hyp = math.sqrt(num1**2 + num2**2)
    return hyp


def hypothenuse():
    num1 = float(input("Enter side 1: "))
    num2 = float(input("Enter side 2: "))

    print(f"The hypothenuse is {calculate_hypothenuse(num1, num2)}")
