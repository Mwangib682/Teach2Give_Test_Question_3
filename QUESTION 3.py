"""
QUESTION 3: Write a Python function to check whether a string is pangram or not. (Assume
the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the
alphabet at least once. For example: The quick brown fox jumps over the
lazy dog.
"""

#defining a new function named is_pangram
def is_pangram(s):
    # Converting the string to lowercase
    s = s.lower()

    # Creating a set of all letters in the English alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    # Create a set of unique letters from the input string
    letters_in_string = set(s)

    # Checking if all alphabet letters are in the letters of the input string
    return alphabet.issubset(letters_in_string)


# Testing examples

print("'Teach2give.' This is a pangram statement: ", is_pangram("Teach2give")) # False
print("'The quick brown fox jumps over the lazy dog.' This is a pangram statement: ", is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print("'Hello world.' This is a pangram statement: ",is_pangram("Hello world"))  # False
print("'Embarrassment.' This is a pangram statement: ",is_pangram("Embarrassment"))  # False
print("'The five boxing wizards jump quickly.' This is a pangram statement: ",is_pangram("The five boxing wizards jump quickly."))  # True
print("'This sentence is missing some letters.' This is a pangram statement: ",is_pangram("This sentence is missing some letters."))  # False


"""
My pycharm IDE results are as follows:
C:\Users\hp\PycharmProjects\pythonProject2\.venv\Scripts\python.exe "C:\Users\hp\PycharmProjects\pythonProject2\QUESTION 3.py" 
'Teach2give.' This is a pangram statement:  False
'The quick brown fox jumps over the lazy dog.' This is a pangram statement:  True
'Hello world.' This is a pangram statement:  False
'Embarrassment.' This is a pangram statement:  False
'The five boxing wizards jump quickly.' This is a pangram statement:  True
'This sentence is missing some letters.' This is a pangram statement:  False

Process finished with exit code 0
"""