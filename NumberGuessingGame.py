# Importing required modules
import random
import math

# Asking user how many times he want to play the game
t=int(input("How many times do you want to play the game? "))
while(t>0):
    # Taking inputs from the user
    lower = int(input("Enter your lower bound: "))
    upper = int(input("Enter your upper bound: "))

    # Generating random number between the lower and upper bounds
    x = random.randint(lower, upper)
    print("\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the correct integer !\n")
    
    # Initializing the number of guesses
    count = 0
    
    # for calculation of minimum number of guesses, it depends upon range
    while count < math.log(upper - lower + 1, 2):
	    count += 1
	    # Asking user to guess any number
	    guess = int(input("Guess any number of your choice: "))
	    # Condition testing
	    if x == guess:
		    print("Congratulations you did it in ", count, " guess!")
		    # Once guessed, loop will break
		    break
	    elif x > guess:
		    print("You guessed too small!")
	    elif x < guess:
		    print("You guessed too high!")
    # If Guessing is more than required guesses,
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
	    print("\nThe number is %d" % x)
	    print("\nBetter Luck Next time!")
    t-=1
"""
PS C:\Users\Charani Veerla\OneDrive\Desktop\Charani\Python Programming in VSC>  c:; cd 'c:\Users\Charani Veerla\OneDrive\Desktop\Charani\Python Programming in VSC'; & 'C:\msys64\mingw64\bin\python.exe' 'C:\Users\Charani Veerla\.vscode\extensions\ms-python.python-2021.6.944021595\pythonFiles\lib\python\debugpy\launcher' '56162' '--' 'c:\Users\Charani Veerla\OneDrive\Desktop\Charani\Python Programming in VSC\NumberGuessingGame.py' 
How many times do you want to play the game? 3
Enter your lower bound: 10
Enter your upper bound: 20

        You've only  3  chances to guess the correct integer !

Guess any number of your choice: 15
You guessed too high!
Guess any number of your choice: 13
You guessed too high!
Guess any number of your choice: 11
You guessed too small!
Guess any number of your choice: 12
Congratulations you did it in  4  guess!

The number is 12

Better Luck Next time!
Enter your lower bound: 20
Enter your upper bound: 22

        You've only  2  chances to guess the correct integer !

Guess any number of your choice: 21
You guessed too high!
Guess any number of your choice: 20
Congratulations you did it in  2  guess!

The number is 20

Better Luck Next time!
Enter your lower bound: 100
Enter your upper bound: 190

        You've only  7  chances to guess the correct integer !

Guess any number of your choice: 100
You guessed too small!
Guess any number of your choice: 119
You guessed too small!
Guess any number of your choice: 121
You guessed too small!
Guess any number of your choice: 131
You guessed too small!
Guess any number of your choice: 141
You guessed too small!
Guess any number of your choice: 151
You guessed too small!
Guess any number of your choice: 166
You guessed too small!

The number is 173

Better Luck Next time!
"""
