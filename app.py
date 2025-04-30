from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_very_secret_key'
app.config['DATABASE'] = 'atm.db'

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    atm_number = request.form['atm_number']
    fingerprint = request.form['fingerprint'] #already written, change nahi kar sakti for prototype
    pin = request.form['pin']

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE atm_number = ?", (atm_number,)).fetchone()

    if not user:
        return render_template('login.html', error="Invalid ATM Number.")

    # Simulate fingerprint verification (in a real system, this would be much more complex)
    if fingerprint != "12345":
        return render_template('login.html', error="Fingerprint verification failed.")

    if not check_password_hash(user['hashed_pin'], pin):
        return render_template('login.html', error="Invalid PIN.")

    session['user_id'] = user['id']
    session['authenticated'] = True
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    return render_template('dashboard.html')

@app.route('/balance')
def balance():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    db = get_db()
    user = db.execute("SELECT balance FROM users WHERE id = ?", (session['user_id'],)).fetchone()
    return render_template('balance.html', balance=user['balance'])

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('withdraw.html', error="Please enter a positive amount.")
            db = get_db()
            cursor = db.cursor() 
            cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ? AND balance >= ?", (amount, session['user_id'], amount))
            db.commit()
            if cursor.rowcount > 0:
                return render_template('withdraw.html', message=f"Rs.{amount:.2f} withdrawn successfully.")
            else:
                return render_template('withdraw.html', error="Insufficient balance.")
        except ValueError:
            return render_template('withdraw.html', error="Invalid amount.")
    return render_template('withdraw.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                return render_template('deposit.html', error="Please enter a positive amount.")
            db = get_db()
            user_id = session['user_id']
            db.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user_id))
            db.commit()
            return render_template('deposit.html', message=f"Rs.{amount:.2f} deposited successfully.")
        except ValueError:
            return render_template('deposit.html', error="Invalid amount.")
    return render_template('deposit.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('authenticated', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)