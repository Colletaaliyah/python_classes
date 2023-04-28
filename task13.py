#Write a program that takes the email and password as input from a user 
# and checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.

for i in range (3):
    email = input('Enter email: ')
    password = input('Enter password: ')
    if email != ('admin@gmail.com') and password != ('Admin@123'):
        print('Invalid Username or Password!')
        continue
    if email == ('admin@gmail.com') and password != ('Admin@123'):
        print('Invalid Username or Password!')
        continue
    if email != ('admin@gmail.com') and password == ('Admin@123'):
        print('Invalid Username or Password!')
        continue
    if email == ('admin@gmail.com') and password == ('Admin@123'):
        print('Login Successful!')
        break
        
else:
    print('Account Blocked!')