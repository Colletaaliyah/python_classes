#  Write a program that takes input of someone's basic salary and benefits, adds them to find the gross 
# salary then uses  the gross salary to find the NHIF. 

# basicsalary = float(input('Enter basic salary: '))
# benefits = float(input('Enter benefits: '))
# gross_salary = basicsalary + benefits
# if gross_salary < 5999:
#     print('150')
# elif gross_salary>=6000 and gross_salary<=7999:
#     print('300')
# elif gross_salary>=8000 and gross_salary<=11999:
#     print('400')
# elif gross_salary>=12000 and gross_salary<=14999:
#     print('500')
# elif gross_salary>=15000 and gross_salary<=19999:
#     print('600')
# elif gross_salary>=20000 and gross_salary<=24999:
#     print('750')
# elif gross_salary>=25000 and gross_salary<=29999:
#     print('850')
# elif gross_salary>=30000 and gross_salary<=34999:
#     print('900')
# elif gross_salary>=35000 and gross_salary<=44999:
#     print('1000')
# elif gross_salary>=45000 and gross_salary<=49999:
#     print('1100')
# elif gross_salary>=50000 and gross_salary<=59999:
#     print('1200')
# elif gross_salary>=60000 and gross_salary<=9999:
#     print('1300')
# elif gross_salary>=70000 and gross_salary<=79999:
#     print('1400')
# elif gross_salary>=80000 and gross_salary<=89999:
#     print('1500')
# elif gross_salary>=90000 and gross_salary<=99999:
#     print('1600')
# else:
#     print('1700')

def calculate_nhif(salary, benefits):
    salary = float(input("Enter salary: "))
    benefits = float(input("Enter benefits: "))
    grosss_salary = salary + benefits
    # nhif = calculate_nhif("salary", "benefits")
    # return (nhif)

    if grosss_salary < 5999:
        nhif = 150
    else:
        if grosss_salary <= 7999:
            nhif = 300
        else:
            if grosss_salary <= 11999:
                nhif = 400
            else:
                if grosss_salary <= 14999:nhif = 500
                else:
                    if grosss_salary <= 19999:
                        nhif = 600
                    else:
                        if grosss_salary <= 29999:
                            nhif = 750
                        else:
                            if grosss_salary <= 34999:
                                nhif = 900
                            else:
                                if grosss_salary <= 39999:
                                    nhif = 950
                                else:
                                    if grosss_salary <= 44999:
                                        nhif = 1000
                                    else:
                                        if grosss_salary <= 49999:
                                            nhif = 1100
                                        else:
                                            if grosss_salary <= 59999:
                                                nhif = 1200
                                            else:
                                                if grosss_salary <= 69999:
                                                    nhif = 1300
                                                else:
                                                    if grosss_salary <= 79999:
                                                        nhif = 1400
                                                    else: 
                                                        if grosss_salary <= 89999:
                                                            nhif = 1500
                                                        else:
                                                            if grosss_salary <= 99999:
                                                                nhif = 1600
                                                            else:
                                                                nhif = 1700
                                                                
                                                                

    return (nhif)
nhif = calculate_nhif("salary", "benefits")
print("NHIF =", nhif)




