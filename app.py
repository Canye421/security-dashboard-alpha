import sqlite3
from datetime import datetime

connection = sqlite3.connect('security_log.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS access_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_time TEXT NOT NULL,
    event_type TEXT NOT NULL
)
''')

current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
event = "System Heratbeat Check"

cursor.execute('''
INSERT INTO access_logs (event_time, event_type)
VALUES (?, ?)
''', (current, event))

connection.commit()

cursor.execute('SELECT * FROM access_logs')
raws = cursor.fetchall()

print("---Current Security Logs---")
for row in raws:
    print(f"ID: {row[0]}, Time: {row[1]}, Event: {row[2]}")
connection.close()

