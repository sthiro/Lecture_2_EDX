# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
# Vowel => {A,E,I,O,U}

s =  input("Input: ")

print("Output: ", end="")

for c in s:
    if c.casefold() not in ["a", "e", "i", "o", "u"]:
        print(c, end="")