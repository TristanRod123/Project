
def after_basePay(wage, hours):
    basePay = float(wage) * float(hours)
    incomePay = basePay * .11
    ssPay = basePay * .062
    medPay = basePay * .0145
    pay = round(basePay - (incomePay + ssPay + medPay),2)
    return pay
    
    

