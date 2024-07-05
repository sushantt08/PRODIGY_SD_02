import random

def main():
    random.seed()
    randomNumber = random.randint(1, 100)
    userGuess = 0
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    print("Can you guess what it is?")

    while userGuess != randomNumber:
        userGuess = int(input("Enter your guess: "))
        attempts += 1

        if userGuess > randomNumber:
            print("Too high! Try again.")
        elif userGuess < randomNumber:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            print(f"It took you {attempts} attempts.")

if __name__ == "__main__":
    main()
