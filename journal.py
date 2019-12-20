import sqlite3
from datetime import date
import os


class PyJournal:
    def __init__(self):
        # os.chdir()
        self.today = date.today().strftime("%B %d, %Y")
        self.db = sqlite3.connect('Database.db', check_same_thread=False)
        self.database = self.db.cursor()

        self.database.execute(
            '''CREATE TABLE if not exists entries(date text primary key, text text)''')

        # self.database.execute('''INSERT INTO entries VALUES ("October 21, 2019", "This is the initial note"), ("December 19, 2019", "This is the new note and its was updated to today"), ("December 16, 2019", "This is the new note and its was updated to today")''')
        self.db.commit()
        self.database.execute(
            "Select text from entries where date = :date", {"date": self.today})
        if not (self.database.fetchall()):
            self.database.execute("Insert into entries values(?, ?)", (
                self.today, "It looks like you don't have any notes yet"))
            self.db.commit()

    def add_note(self, text):
        self.database.execute(
            "Select text from entries where date = :date", {"date": self.today})
        if (self.database.fetchall()):
            self.database.execute("update entries set text = :text where date = :date", {
                                  "text": text, "date": self.today})
            self.db.commit()
        else:
            self.database.execute(
                "Insert into entries values(?, ?)", (self.today, text,))
            self.db.commit()

    def remove_note(self, date):
        self.database.execute(
            "Delete from entries where date = :date", {"date": date})
        self.db.commit()

    def get_today(self):
        self.result = self.database.execute(
            "Select text from entries where date = :date", {"date": self.today})
        return self.result.fetchone()

    def remove_today(self):
        self.database.execute(
            "Delete from entries where date = :date", {"date": self.today})
        self.db.commit()

    def get_entry(self, date):
        self.result = self.database.execute(
            "Select text from entries where date = :date", {"date": date})
        return self.result
