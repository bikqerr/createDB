import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)')
db.execute('INSERT INTO contacts(name, phone, email) VALUES("Ludo", 6545678, "ludo@email.com")')
db.execute('INSERT INTO contacts VALUES("Brian", 1234, "brian@mymail.com") ')

cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')

# print(cursor.fetchall())
print(cursor.fetchone())
print('*' * 30)

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('=' * 30)

cursor.close()
db.close()
