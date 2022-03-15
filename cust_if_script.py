#!/usr/bin/env python3
"""Matt Thurman sample program
   if, elif, else - A simple program for fun!"""


answer = '\n\n
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n
*  Correct!  I am impressed with your English and counting skills!  *\n
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n'

#Ask for response for most common letter in example sentence
response = input("\n\n
        What is the most common letter in the following sentence:\n\n
        __________________________________________________________________\n
        |                                                                |\n
        |  The white elephant ran around the room with a green balloon.  |\n
        |________________________________________________________________|\n\n

        Answer: ")

# if input is e, then celebration prompt appears.  Otherwise different prompts appear depending on how close user was
if response == 'e':
    answer = answer
    print(answer)
elif response == 'n':
    answer = 'Ooh, very close!  This letter appears 5 times, but there is still a letter that appears more often.'
    print(answer)
elif response == 'o':
    answer = 'Ooh, very close!  This letter appears 5 times, but there is still a letter that appears more often.'
    print(answer)
elif response == 't':
    answer = 'Ooh, very close!  This letter appears 5 times, but there is still a letter that appears more often.'
    print(answer)
elif response == 'a':
    answer = 'Ooh, very close!  This letter appears 5 times, but there is still a letter that appears more often.'
    print(answer)
else:
    answer = 'Perhaps you need to take some more time to count the letters...\n\n'
    print('Really?!?!', response, '?\n\n')
    print(answer)
    secondtry = input('Would you like a second try?  Type "y" for yes or "n" for no: ')
    if secondtry == 'y':
        print('\n\nHa!  Nice try.  There are no second chances in this program.  Rerun the program if you would like to try again.')
    elif secondtry == 'n':
        print('\n\nWell you can always rerun the program if you change your mind.')
    else:
        print('\n\nYou didn\'t give me a valid answer!  Please rerun the program...')

print('\n\nGoodbye!\n\n')
