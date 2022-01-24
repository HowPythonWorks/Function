# 1
# https://www.codewars.com/kata/523b4ff7adca849afe000035
# Make a simple function called greet that returns the most-famous "hello world!".

################################

# 2
# https://www.codewars.com/kata/551b4501ac0447318f0009cd
# Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    pass


boolean_to_string(True)  # "True"
boolean_to_string(False)  # "False"

################################

# 3
# Write a function that computes the volume of a sphere given its radius.


def val(rad):
    pass


print(val(5))  # 2617.993877991494

################################

# 4
# Write a function that checks whether a number is in a given range (Inclusive of high and low)


def ran_check(num, low, high):
    pass


print(ran_check(5, 1, 10))  # True
print(ran_check(20, 1, 10))  # False

################################

# 5
# https://www.codewars.com/kata/53af2b8861023f1d88000832
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:


def are_you_playing_banjo(name):
    pass


are_you_playing_banjo("martin")  # "martin does not play banjo");
are_you_playing_banjo("Rikke")  # "Rikke plays banjo");
are_you_playing_banjo("bravo")  # "bravo does not play banjo")
are_you_playing_banjo("rolf")  # "rolf plays banjo")


################################

# 6
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order. Essentially,
# rearrange the digits to create the highest possible number.


def descending_order(num):
    pass


print(descending_order(0))  # 0
print(descending_order(578))  # 875
print(descending_order(123456789))  # 987654321
