from flask import Flask, render_template, request
from datetime import date
import time
import sqlite3
import os
from journal import PyJournal


os.chdir("C:\\Users\\Known_Stranger\\Desktop\\PyDairy\\PyJournal")


app = Flask(__name__)
pyjournal = PyJournal()


@app.route('/')
def index():
    text = pyjournal.get_today()
    print(text[0])
    return render_template('dairy.html', date=pyjournal.today, data=text[0].strip())


@app.route('/post', methods=['POST'])
def display_dairy():
    if request.method == 'POST':
        updated_data = request.form['data']
        pyjournal.add_note(updated_data.rstrip())
        return render_template('dairy.html', date=pyjournal.today, data=updated_data.strip())


if __name__ == '__main__':
    app.run(debug=True)
