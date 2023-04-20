from flask import Flask, render_template, request, redirect, url_for

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
            return redirect(url_for('login'))
    return render_template('home.html')
   
@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/calculate')
def calculate():
    return render_template('calculate.html')

if(__name__ == "__main__"):
    app.run(debug = True)