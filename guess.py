import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("You got it!")