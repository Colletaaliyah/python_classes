# Write a program which accepts email as form input or from terminal.
#  Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use logical operators to solve this.
email = input('Enter email: ')
if '@' in email and '.' in email:
    print('Valid!')
else:
    print('Invalid!')
