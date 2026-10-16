from salary import gross_salary, deductions, net_salary

basic = float(input("Basic salary: "))
hra = float(input("HRA: "))
allowance = float(input("Other allowance: "))
pf = float(input("PF deduction: "))
tax = float(input("Tax deduction: "))
print("Gross salary:", gross_salary(basic, hra, allowance))
print("Deductions:", deductions(pf, tax))
print("Net salary:", net_salary(basic, hra, allowance, pf, tax))
