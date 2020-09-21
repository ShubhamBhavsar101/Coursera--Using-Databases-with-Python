import json
import sqlite3

conn = sqlite3.connect('Assignment4.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Please enter File name')
if len(fname) < 1 : fname = "roster_data.json"

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (entry[0],))
    cur.execute('''SELECT id from User WHERE name = ?''',(entry[0],))
    user_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Course (title) VALUES ( ? )''',(entry[1],))
    cur.execute(''' Select id FROM Course WHERE title = ? ''',(entry[1],))
    course_id = cur.fetchone()[0]

    cur.execute(''' INSERT INTO Member (user_id, course_id, role) Values (?,?,?) ''', (user_id, course_id, entry[2]))

    conn.commit()
