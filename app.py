from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {}

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists.')
        else:
            users[username] = password
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    flash('Please log in first.')
    return redirect(url_for('login'))

@app.route('/animals')
def animals():
    if 'username' in session:
        print(f"User in session: {session['username']}")
        return render_template('animals.html', username=session['username'])
    flash('Please log in first.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
