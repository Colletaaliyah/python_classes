# basicsalary = float(input('Enter basic salary: '))
# benefits = float(input('Enter benefits: '))
# gross_salary = basicsalary + benefits
# NSSF = gross_salary*0.06
# if gross_salary < 5999:
#     print('150')
#     print('NSSF=',NSSF)
# elif gross_salary>=6000 and gross_salary<=7999:
#     print('300')
#     print('NSSF=',NSSF)
# elif gross_salary>=8000 and gross_salary<=11999:
#     print('400')
#     print('NSSF=',NSSF)
# elif gross_salary>=12000 and gross_salary<=14999:
#     print('500')
#     print('NSSF=',NSSF)
# elif gross_salary>=15000 and gross_salary<=19999:
#     print('600')
#     print('NSSF=',NSSF)
# elif gross_salary>=20000 and gross_salary<=24999:
#     print('750')
#     print('NSSF=',NSSF)
# elif gross_salary>=25000 and gross_salary<=29999:
#     print('850')
#     print('NSSF=',NSSF)
# elif gross_salary>=30000 and gross_salary<=34999:
#     print('900')
#     print('NSSF=',NSSF)
# elif gross_salary>=35000 and gross_salary<=44999:
#     print('1000')
#     print('NSSF=',NSSF)
# elif gross_salary>=45000 and gross_salary<=49999:
#     print('1100')
#     print('NSSF=',NSSF)
# elif gross_salary>=50000 and gross_salary<=59999:
#     print('1200')
#     print('NSSF=',NSSF)
# elif gross_salary>=60000 and gross_salary<=9999:
#     print('1300')
#     print('NSSF=',NSSF)
# elif gross_salary>=70000 and gross_salary<=79999:
#     print('1400')
#     print('NSSF=',NSSF)
# elif gross_salary>=80000 and gross_salary<=89999:
#     print('1500')
#     print('NSSF=',NSSF)
# elif gross_salary>=90000 and gross_salary<=99999:
#     print('1600')
#     print('NSSF=',NSSF)
# else:
#     print('1700')
#     print('NSSF=',NSSF)

# def calculator(salary, benefits):
#     nssf = (salary + benefits)*0.06
#     return (nssf)

def calculate_gross_salary(salary, benefits):
    gross_salary = salary + benefits
    return(gross_salary)
def calculate_nssf(gross_salary):
    nssf_rate = 0.06 
    max_deductible_nssf = 18000
    nssf = min((grosss_salary * nssf_rate), max_deductible_nssf)

    return (nssf)
salary = float(input("Enter salary: "))
benefits = float(input("Enter benefits: "))
gs = calculate_gross_salary(salary,benefits)


nssf = calculate_nssf(gs*0.06)
print("NSSF =", nssf)
