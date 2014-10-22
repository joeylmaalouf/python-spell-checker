# JLM - Python Spell Checker
# Copyright (c) 2014 Joey Luke Maalouf

# import our regex package for parsing our input, and the system package to quit
import re
import sys


# -- attempt to open a file ----------------------------------------------------
# Use the built-in 'open' command, with some error handling.
def open_file(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print('Sorry, no file was found with the name \'%s\'.\n' % filename +
              'Please check your file\'s name and re-run the program.')
        sys.exit(1);
    return f

# -- get user input ------------------------------------------------------------
# Ask the user for the file names, and use the defaults if input is left blank.
print('Text File Spell Checker');
f1 = input('\nPlease enter the filename of the word list.\n' +
           '    (Leave blank to use \'wordsEN.txt\'): ')
if f1 == '':
    f1 = 'wordsEN.txt'
f2 = input('\nPlease enter the filename to check for incorrect spelling.\n' +
           '    (Leave blank to use \'check.txt\'): ')
if f2 == '':
    f2 = 'check.txt'
print('\nChecking input file \'%s\' against list file \'%s\':' % (f1, f2))

# -- process the file of acceptable words --------------------------------------
# Open the file with acceptable words and read them into a list, then remove any
# string in the list that evaluates to false (i.e. '') via list comprehensions.
# Make everything lowercase for case-insensitive comparisons later, and add the
# basic letters of the alphabet to the list as well.
text_file = open_file(f1)
word_list = text_file.read().split('\n')
word_list = [word.lower() for word in word_list if word]
word_list.extend(list('abcdefghijklmnopqrstuvwxyz'))

# -- process the file of words to check ----------------------------------------
# Open the file with words to check, then use regex with word boundaries
# to get a list of all the individual words.
check_file = open_file(f2)
to_check = re.findall(r'\b[a-zA-Z0-9]+\b', check_file.read())

# -- check for any incorrect words ---------------------------------------------
# For every word we found in the input file, if the word to check is neither in
# our acceptable list nor a pure number, add it to the list of incorrect words.
# This way, we can mark both 'phone' and '75' as correct, but not 'phone75'.
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

# -- print out our final output ------------------------------------------------
# For every word in the output, tell the user which word was incorrect, as well
# as its numerical index (position) in the input file.
for word in output:
    print('Found unknown word \'%s\' at position %d.' %
          (word, to_check.index(word)))
print('\nEnd of program.\n')
