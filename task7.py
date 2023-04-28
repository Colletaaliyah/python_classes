# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

mark = float(input('Enter student mark: '))
if  mark<0 or mark>100:
        print('invalid input')
else:
    if mark<40:
        print('E')
    else:
        if mark>=40 and mark <=49:
            print('D')
        else: 
            if mark>=49 and mark<=59:
                print('C')
            else:
                if mark>=60 and mark<=79:
                    print('B')
                else:
                    print('A')