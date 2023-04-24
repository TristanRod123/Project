
class Employee:
    def __init__(self, id, firstName, lastName, hours, wage, endDate, payout):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hours = hours
        self.wage = wage
        self.endDate = endDate
        self.payout = payout

    def writeToFile(self, filename):
        information = f"{self.id}:{self.firstName}:{self.lastName}:{self.hours}:{self.wage}:{self.endDate}:{self.payout}"
        with open(filename, 'w') as f:
            f.write(information + '\n')
    
    def employee_exists(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                fields = line.strip().split(':')
                if fields[0] == self.id and fields[5] == self.endDate:
                    return True
        return False