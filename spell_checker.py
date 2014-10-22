# Joey L. Maalouf
# Python Spell Checker

# import our regex package for parsing our input
import re

# -- get user input for filenames ----------------------------------------------
f1 = input(
    "Please enter the filename of the word list. Leave blank for wordsEN.txt")
f2 = input(
    "Please enter the filename of the text to check. Leave blank for check.txt")
if f1 == '':
    f1 = 'wordsEN.txt'
if f2 == '':
    f2 = 'check.txt'

# -- process the file of acceptable words --------------------------------------
# Open the file with acceptable words and read them into a list, then remove any
# string in the list that evaluates to false (i.e. '') via list comprehensions.
# Make everything lowercase for case-insensitive comparisons later, and add the
# basic letters of the alphabet to the list as well.
text_file = open(f1)
word_list = text_file.read().split('\n')
word_list = [word.lower() for word in word_list if word]
word_list.extend(list('abcdefghijklmnopqrstuvwxyz'))

# -- process the file of words to check ----------------------------------------
# Open the file with words to check, then use regex with word boundaries
# to get a list of all the individual words.
check_file = open(f2)
to_check = re.findall(r"\b[a-zA-Z0-9]+\b", check_file.read())

# -- check for any incorrect words ---------------------------------------------
# For every word we found in the input file, if the word to check is neither in
# our acceptable list nor a pure number, add it to the list of incorrect words.
# This way, we can mark both 'phone' and '4' as correct, but not 'phone4'.
incorrect = []
for word in to_check:
    if not (word.lower() in word_list or word.isnumeric()):
        incorrect.append(word)

# -- remove duplicates from the list -------------------------------------------
# For every word in the incorrect list, if it's not already in our output list,
# add it; if it is, then it's a duplicate and we don't care about it.
output = []
for word in incorrect:
    if word not in output:
        output.append(word)

# print out our final output
print(output)
