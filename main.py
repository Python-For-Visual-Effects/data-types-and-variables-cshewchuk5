"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32) 

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number_one = 64
number_two = 32

print(number_one + number_two)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
name = "Chris"
age = 23
money = 1.55

print("My name is " + name + ", I am " + str(age) + " and I only have $" + str(money) + " for coffee.")
# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program."

print len(sentence)


# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
overscan = 0.10 
width = 1920 
height = 1080

print "The 10% overscan of 1920 is " + str(width * overscan) + " and the 1080 is " + str(height * overscan)
#Wasn't sure if I was just meant to find the % of the WxH individually. Sorry if I misinterpreted, my fault! 
