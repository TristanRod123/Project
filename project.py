from distutils.file_util import write_file
from flask import Flask, render_template, request, redirect, url_for, session, flash
from stuff.display import *
from stuff.employee import *
from stuff.payroll import *
from stuff.employer import *

app = Flask(__name__)
app.secret_key = "purple"

@app.route('/')
def loginPage():
    return redirect(url_for('login'))
   
@app.route('/login', methods =['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != employer1.get_username():
            error = 'Invalid Credentials. Please try again.'
            flash('User does not exist!')
            return redirect(url_for('login'))
        elif password != employer1.get_password():
            flash('Password was incorrect!')
            return redirect(url_for('login'))
        else:
            session['employer'] = username
            return redirect(url_for('home'))
    return render_template('base.html', error=error)

@app.route('/logout-user', methods = ['POST', 'GET'])
def logout_user():
    session.pop(employer1.get_username(), None)
    return redirect(url_for('login'))
        

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form['button'] == 'clicked1':
            return redirect(url_for('calculate'))
        if request.form['button'] == 'clicked2':
            return redirect(url_for('history'))
        if request.form['button'] == 'clicked3':
            return redirect(url_for('input'))
    return render_template('home.html')
   
@app.route('/history', methods=['GET','POST'])
def history():
    table_data = []
    if request.method == 'POST':
        if request.form['button'] == 'clicked2': 
            table_data = tableData('employeeInfo.txt', "0")

        if request.form['button'] == 'clicked1':
            date = request.form['date']
            table_data = tableData('employeeInfo.txt', date)


    return render_template('history.html', table_data=table_data)

@app.route('/calculate', methods = ['GET','POST'])
def calculate():
    message = ''
    if request.method == 'POST':
        wage = request.form['Wage']
        hours = request.form['Hours'] 
        pay = after_basePay(wage,hours)
        message = f"Payout: {str(pay)}"

    return render_template('calculate.html', message=message)

@app.route('/input', methods =['GET','POST'])
def input():
    message = ''
    if request.method == 'POST':
        id = request.form['Id']
        first_name = request.form['fName']
        last_name = request.form['lName']
        hours = request.form['Hours']
        wage = request.form['Wage']
        end_date = request.form['date']
        basepay = float(hours) * float(wage)
        payout = 0

        new_employee = Employee(id, first_name, last_name, hours, wage, end_date, basepay, payout)
        employeeFile = "employeeInfo.txt"
        if (new_employee.employee_exists(employeeFile)):
            message = "Employee already exists"
        else:
            new_employee.writeToFile(employeeFile)
            message = "Employee added successfully"
        
    return render_template('input.html', message=message)

if(__name__ == "__main__"):
    app.run(debug = True)

