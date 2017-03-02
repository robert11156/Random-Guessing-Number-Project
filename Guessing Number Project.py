# The computer picks a random number between 1 and 100
# the player know if the guess is too high, too low
# or guess the number correctly
import random

the_number = random.randint(1, 100)
name = input("Enter your name: ")
print("Hi," ,name, " I am thinking of a number between 1 and 100. Guess the number")

#guessestaken
print("Welcome to my Guessing Game.")


tries = 0

# guessing loop
while tries <6:
    guess = int(input("Guess the number: "))
    tries = tries+1 
    if guess > the_number:
        print("The number is too large")
    elif guess < the_number:
        print("The number is too small")
    if guess == the_number:
        print("You have guess the correct number, Congrats")
          
