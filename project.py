from distutils.file_util import write_file
from flask import Flask, render_template, request, redirect, url_for
from stuff.display import *
from stuff.employee import *
from stuff.payroll import *


app = Flask(__name__)

@app.route('/')
def loginPage():
    return redirect(url_for('login'))
   
@app.route('/login', methods =['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('base.html', error=error)
        

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
   
@app.route('/history')
def history():
    if request.method == 'POST':
        if request.form['button'] == 'clicked1': 
            id = request.form['Id']
            displayHistory('employeeInfo.txt',id)
        if request.form['date'] == 'clicked2':
            date = request.form['date']
            displayAllHistory('employeeInfo.txt',date)
    return render_template('history.html')

@app.route('/calculate')
def calculate():
    if request.method == 'POST':
        id = request.form['Id']
        date = request.form['date'] 
        pay = updatePayout('employeeInfo.txt',id,date)

    return render_template('calculate.html')

@app.route('/input', methods =['GET','POST'])
def input():
    if request.method == 'POST':
        id = request.form['Id']
        first_name = request.form['fName']
        last_name = request.form['lName']
        hours = request.form['Hours']
        wage = request.form['Wage']
        end_date = request.form['date']
        payout = 'N/A'

        new_employee = Employee(id, first_name, last_name, hours, wage, end_date, payout)
        employeeFile = "Project\stuff\employeeInfo.txt"
        if (new_employee.employee_exists(employeeFile)):
            return "Employee already exists"
        else:
            new_employee.writeToFile(employeeFile)
        #return some response to the client
            return "Employee added successfully"
        
    return render_template('input.html',)

if(__name__ == "__main__"):
    app.run(debug = True)