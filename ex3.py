import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
#print("Opened database successfully")


#CREATING THE TABLE AADHAR
#cursor.execute('''CREATE TABLE AADHAR
#         (
#         NAME           TEXT    NOT NULL,
#        AADHAR         INT     NOT NULL);
#         ''')

#INSERTING THE DATA INTO TABLE
#cursor.execute("INSERT INTO AADHAR (NAME, AADHAR) \
#      VALUES ('Rohan', 123456789)")
#cursor.execute("INSERT INTO AADHAR (NAME, AADHAR) \
#      VALUES ('Allen', 23456789)")
#cursor.execute("INSERT INTO AADHAR (NAME, AADHAR) \
#      VALUES ('Martha', 345678910)")
#cursor.execute("INSERT INTO AADHAR (NAME, AADHAR) \
#     VALUES ('Palak', 4567891023)")

#SELECTING THE PARTICULAR FROM THE TABLE

for row in cursor.execute("SELECT NAME, AADHAR from AADHAR"):
    print("NAME = ", row[0])
    print(("AADHAR = ", row[1]),"\n")


cursor.close()
conn.commit()
conn.close()
