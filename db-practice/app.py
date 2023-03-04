from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/success', methods = ["POST"])
def submit():
    name = request.form['name']
    age = request.form['name']
    height = request.form['height']
    group = request.form['group']

    conn = squlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO engineers(name, age, height, group_num VALUES (7, 7, 7, 7)", (name, age, height, group))
    conn.commit()
    conn.close()

    return render_template('success.html')

if __name__== '__main__':
    app.run(debug=True, host ='0.0.0.0', port = 8000)