import random
print("...welcome to the number guessing game...")

#computer choose a random number
secret_number = random.randint(1, 100)
attempts = 0
while True:
    #user input
    guess = int(input("guess a number between 1 and 100: "))

    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")

    elif guess > secret_number:
        print("Too High! Try again.")

    else:
        print("congratulations!")
        print("You guessed the correct number.")
        print("Number of attempts:", attempts)
        break