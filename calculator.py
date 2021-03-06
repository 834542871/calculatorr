#!/usr/bin/env python3
import sys

class ParameterNumError:
    pass
def get_tax(salry_paytax):
    employee_paytax = employee.copy()
    for key, value in employee_paytax.items():
        salary_paytax = value * (1 - 0.08 - 0.02 - 0.005 - 0.06) - 3500        
        if salary_paytax <= 0:
            tax = 0.00      
        elif salary_paytax <= 1500.00:
            tax = salary_paytax * 0.03
        elif (salary_paytax  > 1500.00) and (salary_paytax <= 4500.00):
            tax = salary_paytax * 0.1 -105.00
        elif (salary_paytax > 4500.00) and (salary_paytax <= 9000.00):
            tax = salary_paytax * 0.2 -555.00
        elif (salary_paytax > 9000.00) and (salary_paytax <= 35000.00):
            tax = salary_paytax * 0.25 - 1005.00
        elif (salary_paytax > 35000.00) and (salary_paytax <= 55000.00):
            tax = salary_paytax * 0.3 -2755
        elif (salary_paytax > 55000.00) and (salary_paytax <= 80000.00):
            tax = salary_paytax * 0.35 -5505.00
        else:
            tax = salary_paytax * 0.45 -13505.00
        
        employee_paytax[key] = value * (1 - 0.08 - 0.02 - 0.005 - 0.06) - tax
    return employee_paytax

if __name__ == '__main__':
    try:
        employee = {}
        if len(sys.argv) < 2:
            raise ParameterNumError
        for s in sys.argv[1:]:
            data = s.split(':')
            employee[data[0]] = int(data[1])
        employee_paytax = get_tax(employee)
        for key, value in employee_paytax.items():
            print(key + ':' + str(format(value, '.2f')))
    except (ParameterNumError, ValueError):
        print('Parameter Error')

