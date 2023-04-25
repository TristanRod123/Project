
def after_basePay(wage, hours):
    basePay = float(wage) * float(hours)
    incomePay = basePay * .11
    ssPay = basePay * .062
    medPay = basePay * .0145
    pay = round(basePay - (incomePay + ssPay + medPay),2)
    return pay
    
    
# def updatePayout(filename, employee_id, end_date):
#     with open(filename, 'r') as f:
#         lines = f.readlines()

#     with open(filename, 'w') as f:
#         for line in lines:
#             fields = line.strip().split(':')
#             if fields[0] == employee_id and fields[5] == end_date:
#                 basePay = float(fields[3]) * float(fields[4])
#                 newPayout = after_basePay(basePay)
#                 fields[6] = str(newPayout)
#                 line = ':'.join(fields) + '\n'
#                 f.write(line)
#     return newPayout
        
    # for i, line in enumerate(lines):
    #     fields = line.strip().split(':')
    #     if fields[0] == employee_id and fields[5] == end_date:
    #         basePay = float(fields[3]) * float(fields[4])
    #         newPayout = after_basePay(basePay)
    #         fields[6] = str(newPayout)

    #         modified_line = ':'.join(fields) + '\n'
    #         lines[i] = modified_line
    #         with open(filename, 'w') as f:
    #             f.writelines(lines[i])    

