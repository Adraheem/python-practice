from first_class import FirstClass


def get_grade():
    grade = int(float(input("Enter grade: ")))
    counter = 0

    while counter < 3:
        if counter != 0:
            grade = int(float(input("Enter grade again: ")))

        counter += 1

        if grade < 0 or grade > 100:
            print("Invalid input")
        else:
            if 90 <= grade <= 100:
                print("A")
            elif 70 <= grade <= 89:
                print("B")
            elif 50 <= grade <= 69:
                print("C")
            elif 40 <= grade <= 49:
                print("D")
            elif 30 <= grade <= 39:
                print("E")
            else:
                print("F, Zero talent")


if __name__ == '__main__':
    # get_grade()

    my_class = FirstClass("John Doe", 11)
    print(my_class.get_age())
    print(my_class.get_name())

    my_class.set_name("Mat New")
    my_class.set_age(56)

    print(my_class.get_age())
    print(my_class.get_name())

    print(FirstClass.use_static())
