def gross_salary(basic, hra, allowance):
    return basic + hra + allowance

def deductions(pf, tax):
    return pf + tax

def net_salary(basic, hra, allowance, pf, tax):
    return gross_salary(basic, hra, allowance) - deductions(pf, tax)
