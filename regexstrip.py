#! python3
# Program takes predefined strings and trims their beginning and end by characters specified by the user.
# Could easily be combined with pyperclip to also ask user for string input from the clipboard.

import re

print('Enter letters (or spaces) to be removed:')
letters = input()
leadletters = '^[' + letters + ']+'
trailletters = '[' + letters + ']+$'

leadspaceRegex = re.compile(leadletters)
trailspaceRegex = re.compile(trailletters)

def regexstrip(string):
    string = leadspaceRegex.sub('', string)
    string = trailspaceRegex.sub('', string)
    return string

sample1 = '   Hello World!   '
sample2 = 'SpamSpamBaconSpamEggsSpamSpam'

print(sample1)
print('Number of characters:' + str(len(sample1)))
print(regexstrip(sample1))
print('Number of characters:' + str(len(regexstrip(sample1))))

print(sample2)
print('Number of characters:' + str(len(sample2)))
print(regexstrip(sample2))
print('Number of characters:' + str(len(regexstrip(sample2))))
