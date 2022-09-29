import math

if __name__ == '__main__':
    radius_str = input("Enter the radius of your circle: ")
    radius_int = int(radius_str)

    circumference = 2 * math.pi * radius_int
    area = math.pi * (radius_int ** 2)

    print("The circumference is:", circumference,
          ",\nand the area is:", area)

    value = 5
    val = 3
    result = value % val
    print('result -> ', result)
