

def after_basePay(basePay):
    incomePay = basePay * .11
    ssPay = basePay * .062
    medPay = basePay * .0145

    return basePay - (incomePay + ssPay + medPay)
    
    
def updatePayout(filename, employee_id, end_date):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        fields = line.strip().split(':')
        if fields[0] == employee_id and fields[5] == end_date:
            basePay = float(fields[3]) * float(fields[4]) # change to float? as the input is all string
            newPayout = after_basePay(basePay)
            fields[6] = str(newPayout)

            modified_line = ':'.join(fields) + '/n'
            lines[i] = modified_line
            break

    with open(filename, 'w') as f:
        f.writelines(lines)

    

        
