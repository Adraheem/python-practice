import random

if __name__ == '__main__':
    number = random.randint(1, 10)
    count = 0
    total_guess = 5

    while count < total_guess:
        print("\nNumber of guesses:", total_guess - count)
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("You guessed right")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        count += 1
    else:
        print("\nYou've run out of guesses!")
