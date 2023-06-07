# This is a brute force function

# Declaring te variables
message = input("Enter the cipher here:")
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to loop the input
for key in range(len(LETTERS)):
    translated = ''
    for i in message:
        if i in LETTERS:
            num = LETTERS.find(i)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + i

# %s in string is to assign the variables accordingly
    print('Hacking key #%s: %s' % (key, translated))
