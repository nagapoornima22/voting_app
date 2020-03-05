import sqlite3

conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()

print('hi, are you looking for vote')
response = input("enter Y or N ")
if response=='N':
    print("Thank you")
else:
    aadhar = int(input("Give your adhar number "))
    name = input("enter your name")
    cursor.execute("SELECT AADHAR from AADHAR where aadhar = ?", (aadhar,))
    #cursor.execute("SELECT NAME from AADHAR where name = ?", (name,))

    rows = cursor.fetchall()
    #print(rows)
    for row in rows:
        if row[0] == aadhar:
            print('aadhar exists')
            break;
    if rows ==[]:
        cursor.execute("INSERT INTO AADHAR (NAME,AADHAR) \
                         VALUES (?, ?)", (name, aadhar))
        print("aadhar added")












    # rows = {row[0] for row in cursor.fetchall()}
    # print(rows)
    # if aadhar in rows:
    #     print("aadhar Taken")
    #
    # else :
    #     print("aadhar added")
    # for row in results:
    #     print(row[0])
    #     if(row[0] == ''):
    #         cursor.execute("INSERT INTO AADHAR (ID,NAME,AADHAR,STATUS) \
    #                                          VALUES (?, ?, ?,  ?)", (6, 'gfhyftyftf', aadhar, 0));
    #         print("aadhar added")
    #
    #
    #     else:
    #         print(row[0])
    #         print("aadhar exists", row[0])




    cursor.close()

    conn.commit()
    conn.close()


