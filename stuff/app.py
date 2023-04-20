from flask import Flask, render_template, request
from employee import *
from employer import *

app = Flask(__name__)

@app.route("/")
def loginPage():
    pass

# def add_employee_route():
#     id = request.form['id']
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     hours = request.form['hours']
#     wage = request.form['wage']
#     end_date = request.form['end_date']
#     payout = "N/A"

#     new_employee = add_employee(id, first_name, last_name, hours, wage, start_date, end_date, payout)

#     writeToFile(employeeInfo.txt, new_employee)
#     # return some response to the client
#     return "Employee added successfully"

if __name__ == "__main__":
    app.run(debug = True)