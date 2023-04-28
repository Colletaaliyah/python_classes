 #Prompt the user for a number either on a form input or the terminal.
#   Depending on whether the number is even or odd, display  either “odd” or “even” 
# to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

number = float(input('enter a number: '))
if number%2 == 0 and number%4 == 0:
        print('Divisible by 4')
if number%2 == 0 and number%4 != 0:
    print('Not divisible by 4')
else:
    print('This is an odd number')