# if 5 < 6:
#     print('executes when true')
#     print('executes also when true')
#     print('executes all also when true')
# else:
#     print('executes when false')
#     print('executes when false')

# print('executes either way')

# mark=int(input('Enter a mark: '))
# if mark >= 70:
#     print('A')
# elif mark >= 60 and mark < 70:
#     print('B')
# elif mark >= 50 and mark < 60:
#     print('C')
# elif mark >= 40 and mark < 50:
#     print('D')
# else:
#     print('E')


# num=int(input('Enter a number: '))
# num2=int(input('Enter a num2: '))
# num3=int(input('Enter a num3: '))
# if num > num2 and num3 :
#     print('largest number is: ',num)
# elif num2 > num3 and num:
#     print('largest number is: ',num2)
# elif num3 > num and num2:
#     print('largest number is: ',num3)



try:
    mark=float(input('Enter a mark: '))
    if  mark<0 or mark>100:
         print('invalid input')
    else:
        if mark <40:
            print('E')
        else:
            if mark>40 and mark <50:
                print('D')
            else: 
                if mark>50 and mark<60:
                    print('C')
                else:
                    if mark >60 and mark<70:
                        print('B')
                    else:
                        print('A')
except Exception as e:
    print(e)

# except:
#     print('ensure your number is an integer')
     
   

                  


                                
                                    
                                    

                                   
                
                
                                    

               