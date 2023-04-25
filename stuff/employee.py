from stuff.payroll import after_basePay

class Employee:
    def __init__(self, id, firstName, lastName, hours, wage, endDate, basepay ,payout):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hours = hours
        self.wage = wage
        self.endDate = endDate
        self.basepay = basepay
        self.payout = payout

    def writeToFile(self, filename):
        total = float(self.wage) * float(self.hours)
        self.payout = after_basePay(float(self.wage), (self.hours))
        information = f"{self.id}:{self.firstName}:{self.lastName}:{self.hours}:{self.wage}:{self.endDate}:{self.basepay}:{self.payout}"
        with open(filename, 'a') as f:
            f.write(information + '\n')
    
    def employee_exists(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                fields = line.strip().split(':')
                if fields[0] == self.id and fields[5] == self.endDate:
                    return True
        return False