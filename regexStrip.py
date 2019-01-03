#! python3
# Program takes predefined strings and trims their beginning and end by characters specified by the user.

import re

print('Enter letters (or spaces) to be removed from beginning and end of string:')
letters = input()
leadletters = '^[' + letters + ']+'
trailletters = '[' + letters + ']+$'

leadspaceRegex = re.compile(leadletters)
trailspaceRegex = re.compile(trailletters)

def regexStrip(string):
    string = leadspaceRegex.sub('', string)
    string = trailspaceRegex.sub('', string)
    return string

sample1 = '   Hello World!   '
sample2 = 'SpamSpamBaconSpamEggsSpamSpam'

print(sample1)
print('Number of characters:' + str(len(sample1)))
print(regexStrip(sample1))
print('Number of characters:' + str(len(regexStrip(sample1))))

print(sample2)
print('Number of characters:' + str(len(sample2)))
print(regexStrip(sample2))
print('Number of characters:' + str(len(regexStrip(sample2))))
