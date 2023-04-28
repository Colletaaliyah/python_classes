# Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01...
#  Convert the number to start with +254… 

Tel = (str(input('Enter phone number: ')))
if str('+254') in Tel[0:4]:
    print('valid!')
elif str('07') in Tel[0:2]:
    Tel=Tel[1: ]
    print('+254'+(Tel))
elif str('01')  in Tel[0:2]:
    Tel=Tel[1: ]
    print('+254'+(Tel))
elif str('71') in Tel[0:2]:
    # Tel=Tel[0: ]
    print('+254'+(Tel))
elif str('254') in Tel[0:3]:
    # Tel=Tel[ : ]
    print('+'+(Tel))

    

    

    