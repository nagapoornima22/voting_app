import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
for row in cursor.execute("SELECT AADHAR from AADHAR where aadhar = ?", (45525566,)):
    print("aadhar exists", row[0])

cursor.close()

conn.commit()
conn.close()

# def enter_dynamic_data():
# lang = input("What language? ")
# version = float(input("What version? "))
# skill = input("What skill level? ")
#
# c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)",
# (lang, version, skill))
#
# conn.commit()


