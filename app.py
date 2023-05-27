from flask import Flask, request, jsonify, render_template, redirect
import sqlite3

app = Flask(__name__, static_url_path='/static')


def create_table():
    conn = sqlite3.connect('bookings.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  phone_number TEXT NOT NULL,
                  start_location TEXT NOT NULL,
                  end_location TEXT NOT NULL,
                  travel_date TEXT NOT NULL,
                  travel_class TEXT NOT NULL,
                  num_seats INTEGER NOT NULL)''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    conn = sqlite3.connect('bookings.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('display_data.html', bookings=bookings)


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone']
    start_location = request.form['from']
    end_location = request.form['to']
    travel_date = request.form['date']
    travel_class = request.form['class']
    num_seats = request.form['seats']

    conn = sqlite3.connect('bookings.db')
    c = conn.cursor()
    c.execute('''INSERT INTO bookings (name, email, phone_number, start_location, end_location, travel_date, travel_class, num_seats)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, email, phone_number, start_location, end_location, travel_date, travel_class, num_seats))
    conn.commit()
    conn.close()

    return redirect('/data')


if __name__ == '__main__':
    create_table()
    app.run(debug=False, port=8000, host='0.0.0.0')
