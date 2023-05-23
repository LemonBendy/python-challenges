import sqlite3

def create_student_table():
    db = "SQL/student.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)''')
    conn.commit()
    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
    c.executemany("INSERT INTO students VALUES (?, ?)", data)
    conn.commit()
    conn.close()

def print_student_table():
    db = "SQL/student.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    print(c.fetchall())
    conn.close()

def show_single_record():
    db = "SQL/student.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    varname = input("Enter name: ")
    sqlstring = "SELECT * FROM students WHERE name = '%s'" % varname
    c.execute(sqlstring)
    print(c.fetchall())
    conn.close()


if __name__ == "__main__":
    print_student_table()
    show_single_record()