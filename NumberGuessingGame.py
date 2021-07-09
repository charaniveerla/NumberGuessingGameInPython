# Importing required modules
import random
import math

# Taking inputs from the user
lower = int(input("Enter your lower bound: "))
upper = int(input("Enter your upper bound: "))

# Generating random number between the lower and upper bounds
x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the correct integer !\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of guesses, it depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1
	# Asking user to guess any number
	guess = int(input("Guess any number of your choice: "))
	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			count, " guess!")
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
