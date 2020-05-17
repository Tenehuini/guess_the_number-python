import sys

from random import randint


if len(sys.argv) > 2:
    print("Only one argument is valid, the max number allowed")
    exit()

max_number = sys.argv[1] if len(sys.argv) == 2 else 9
print(max_number)

try:
    max_number = int(max_number)
except ValueError:
    print("Argument must be a number.")
    exit()

if max_number <= 1:
    print("Number must be positive and higher than 1")
    exit()

random_number = randint(1, max_number)

guess = -1

print("Guess the number, from 1 to {}\n\n".format(max_number))

while guess != random_number:
    guess = int(input("Number: "))
    if guess < random_number:
        print("The number is higher")
    elif guess > random_number:
        print("The number is lower")
    else:
        print("You guessed the number!")
