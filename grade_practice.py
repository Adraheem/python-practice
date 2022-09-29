if __name__ == '__main__':
    grade = int(float(input("Enter grade: ")))
    counter = 0

    while counter < 3:
        counter += 1

        if grade < 0 or grade > 100:
            grade = int(float(input("Invalid grade, enter grade again: ")))
            continue
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

            break
