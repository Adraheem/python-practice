import random


def guess_number():
    random_number = random.randint(1, 1000)

    for i in range(5):
        number = int(input("Guess a number between 1 and 1000: "))
        if number > random_number:
            print("Too high, try again!")
        elif number < random_number:
            print("Too low, try again!")
        else:
            print("Congratulations")
            break
    else:
        print("You failed, you have exceeded your number of guesses")
