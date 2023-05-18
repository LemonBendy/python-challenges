import sqlite3

# Connect to database

def create_table():
    conn = sqlite3.connect('SQL/customer.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER
        (ID  INT    PRIMARY KEY  NOT NULL,
        NAME        TEXT         NOT NULL,
        ROOM         INT          NOT NULL,
        ADDRESS     CHAR(50),
        SALARY      REAL);''')
    print("Table created successfully")
    conn.close()

def insert_data():
    try:
        conn = sqlite3.connect('SQL/customer.db')
        print("Opened database successfully")
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        room = input("Enter Room: ")
        address = input("Enter Address: ")
        salary = input("Enter Salary: ")
        conn.execute("INSERT INTO CUSTOMER (ID,NAME,ROOM,ADDRESS,SALARY) \
            VALUES (?,?,?,?,?)",(id,name,room,address,salary));
        conn.commit()
        print("Records created successfully")
        conn.close()
    except:
        return False

def show_records():
    try:
        conn = sqlite3.connect('SQL/customer.db')
        cursor = conn.execute('''SELECT ID, NAME, ROOM, ADDRESS, SALARY FROM CUSTOMER''')
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ROOM = ", row[2])
            print("ADDRESS = ", row[3])
            print("SALARY = ", row[4], "\n")
            print("Operation done successfully")
            return True
        conn.close()
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    create_table()
    #insert_data()
    show_records()