# password = input('Enter your password: ')
# orpasword=('admin@123')
try:
    password = input('Enter your password: ')
    orpasword=('admin@123')
    if orpasword==password:
        print('correct')
    

    else:
       if password != orpasword:
        input('Enter your password: ')
        if password == orpasword:
            print('correct')
            break
        else:
            if password != orpasword:
                input('Enter your password: ')
                if password == orpasword:
                    print('correct')
                    break
            else: 
                if password != orpasword:
                    input('Enter your password: ')
                    if password == orpasword:
                        print('correct')
                        break
except:
    print('Account blocked!')
                            
                                # except
                                # print('Account blocked!')
