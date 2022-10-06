import math


class AssignmentClass:
    @staticmethod
    def fill_missing_code():
        grade = int(input("Enter grade: "))
        if grade >= 90:
            print(f"Congratulations! Your grade of {grade} earns you an A in this course")
        else:
            print(f"You scored {grade} in this course")

    @staticmethod
    def calculate_eggs():
        eggs = int(input("Enter the number of eggs: "))

        crates = math.ceil(eggs / 6)
        remaining_eggs = eggs % 6
        print(f"{eggs} eggs will occupy {crates} crates with {remaining_eggs} in the last crate")

    @staticmethod
    def bacterial_growth():
        print("Hour \t\t Number of Bacteria")
        for i in range(0, 16, 5):
            num = 200 * 2**i
            print(f"{i} \t\t\t {num}")

    @staticmethod
    def multiplication_table():
        for i in range(1, 11):
            print(f"{i}", end="\t|\t")
            for j in range(1, 11):
                print(f"{j*i}", end="\t")
            print("")

    @staticmethod
    def reverse_number():
        num = input("Enter a number (to reverse with spaces): ")
        num_array = list(num)
        for i in range(len(num_array) - 1, -1, -1):
            print(f"{num_array[i]}", end=" ")

    @staticmethod
    def check_palindrome():
        num = input("Enter a number (check palindrome): ")
        num_array = list(num)
        num_array.reverse()
        rev_num = "".join(num_array)
        print(f"{num} is {'' if num == rev_num else 'not '}a palindrome number")

    @staticmethod
    def fibonacci():
        # generate a list of first 100 fibonacci numbers
        fib = [0, 1]
        for i in range(2, 100):
            n = fib[i-1] + fib[i-2]
            fib.append(n)
        idx = int(input("Enter a number from 0 to 99 (to select fibonacci index): "))
        if idx < 100:
            print(fib[idx])
        else:
            print("Invalid index")

    @staticmethod
    def equilateral_triangle():
        sides = input("Enter the three sides of the triangle (separated by comma): ")
        sides = sides.split(",")
        a = int(sides[0].strip())
        b = int(sides[1].strip())
        c = int(sides[2].strip())

        if a == b and b == c:
            print("Equilateral triangle")
        else:
            print("It is not an equilateral triangle")

    @staticmethod
    def flu_tracker():
        minimum_infected = 0
        max_infected = 0
        total = 0
        for i in range(7):
            num = int(input(f"Enter the number of infected patients for day {i+1}: "))
            total += num
            if i == 0:
                minimum_infected = num
                max_infected = num
            else:
                if num < minimum_infected:
                    minimum_infected = num
                if num > max_infected:
                    max_infected = num

        average = total / 7
        print(f"Total: \t\t\t {total}\n"
              f"Average: \t\t {average}\n"
              f"Minimum: \t\t {minimum_infected}\n"
              f"Maximum: \t\t {max_infected}")

    @staticmethod
    def turing_test():
        input("What is your problem? ")
        answer = ""

        while answer != "yes" and answer != "no":
            answer = input("Have you had this problem before (yes or no)? ")

        if answer == "yes":
            print("Well, you have it again.")
        else:
            print("Well, you have it now.")

    @staticmethod
    def heart_rate_monitor():
        age = int(input("Enter age (for heart rate monitor): "))
        max_heart_rate = 220 - age
        target_heart_rate_l = 0.5 * max_heart_rate
        target_heart_rate_h = 0.85 * max_heart_rate

        print(f"Maximum Heart rate: \t\t {max_heart_rate}\n"
              f"Target heart rate: \t\t\t {target_heart_rate_l} - {target_heart_rate_h}")

    @staticmethod
    def wage_calculator():
        original = 10
        after = original * ((1 + 0.03) ** 5)
        after = after * ((1 - 0.03) ** 2)
        print(f"Wage after the 5 positive and 2 negative reviews -> {after}")
