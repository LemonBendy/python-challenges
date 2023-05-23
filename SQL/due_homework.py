import sqlite3

class homework():
    def __init__(self):
        pass

    def create_table(self):
        try:
            conn = sqlite3.connect('SQL/homework.db')
            print("Opened database successfully")
            conn.execute('''CREATE TABLE IF NOT EXISTS HOMEWORK
                (HOMEWORK CHAR(15) NOT NULL,
                SUBJECT CHAR(10) NOT NULL,
                DUE_DATE DATE NOT NULL);''')
            print("Table created successfully")
            conn.close()
        except Exception as e:
            print(e)
            return False
        
    def insert_data(self):
        try:
            conn = sqlite3.connect('SQL/homework.db')
            print("Opened database successfully")
            homework = input("Enter homework: ")
            subject = input("Enter subject: ")
            due_date = input("Enter due date: ")
            conn.execute("INSERT INTO HOMEWORK (HOMEWORK,SUBJECT,DUE_DATE) \
                VALUES (?,?,?)",(homework,subject,due_date));
            conn.commit()
            print("Records created successfully")
            conn.close()
        except Exception as e:
            print(e)
            return False
        
    def show_records(self):
        try:
            conn = sqlite3.connect('SQL/homework.db')
            cursor = conn.execute('''SELECT HOMEWORK, SUBJECT, DUE_DATE FROM HOMEWORK''')
            for row in cursor:
                print("HOMEWORK = ", row[0])
                print("SUBJECT = ", row[1])
                print("DUE_DATE = ", row[2], "\n")
                print("Operation done successfully")
                return True
            conn.close()
        except Exception as e:
            print(e)
            return False
        
    def search_records(self):
        try:
            conn = sqlite3.connect('SQL/homework.db')
            due_date = input("Enter due date: ")
            cursor = conn.execute('''SELECT HOMEWORK, SUBJECT, DUE_DATE FROM HOMEWORK WHERE DUE_DATE = ?''', (due_date,))
            for row in cursor:
                print("HOMEWORK = ", row[0])
                print("SUBJECT = ", row[1])
                print("DUE_DATE = ", row[2], "\n")
                print("Operation done successfully")
                return True
            conn.close()
        except Exception as e:
            print(e)
            return False
        


if __name__ == "__main__":
    hw = homework()
    hw.create_table()
    hw.insert_data()
    hw.show_records()
    hw.search_records()