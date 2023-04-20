
class Employee:
    def __init__(self, id, firstName, lastName, hours, wage, endDate, payout):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hours = hours
        self.wage = wage
        self.endDate = endDate
        self.payout = payout

    def add_employee(id, first_name, last_name, hours, wage, start_date, end_date, payout):
    # code to add employee to file goes here
        pass

    def to_string(self):
        return f"{self.id}:{self.firstName}:{self.lastName}:{self.hours}:{self.wage}:{self.endDate}:{self.payout}"

    def writeToFile(filename, employeeobj):
        information = employeeobj.to_string()
        with open(filename, 'a') as f:
            f.write(information + '\n')