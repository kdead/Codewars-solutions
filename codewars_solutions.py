# Solution: Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 ==0 else "Odd"

# Convert a Number to String
def number_to_string(num):
    return str(num)

#Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#Vowel Count
def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")

