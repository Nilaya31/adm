import sqlite3

connector = sqlite3.connect('TEACHER.db')
cursor = connector.cursor()
print("Enter 1. To add the student: ")
print("Enter 2. Get the student details: ")
print("Enter 3. Get all student details: ")
print("Enter 4. delete student details: ")
print("Enter 5. Edit the student: ")
print("Enter 6. Exit: ")
a = int(input())
if a == 1:
    print("Enter the name of the student: ")
    Name = input()
    print("Enter the Department_Name: ")
    Department_Name = input()
    print("Enter the Mark_1: ")
    Mark_1 = int(input())
    print("Enter the Mark_2: ")
    Mark_2 = int(input())
    print("Enter the Mark_3: ")
    Mark_3 = int(input())

    total = Mark_1 + Mark_2 + Mark_3
    Average = total / 3
    if Average > 90:
        Grade = "S"
    elif Average > 81:
        Grade = "A"
    elif Average > 71:
        Grade = "B"
    elif Average > 61:
        Grade = "C"
    elif Average > 56:
        Grade = "D"
    elif Average > 50:
        Grade = "E"
    else:
        Grade = "U"
    res = cursor.execute(
        "INSERT INTO student (name,depart,mark1,mark2,mark3,totalmark,average,grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (Name, Department_Name, Mark_1, Mark_2, Mark_3, total, Average, Grade,))
    connector.commit()
    print("Student details Updated")

elif a == 2:
    print("Enter the id of the student: ")
    id = input()
    sql = "select * from student where id = %s"
    cursor.execute(sql, (id,))
    data = cursor.fetchall()
    print(data)


elif a == 3:
    cursor.execute("select * from student")
    output = cursor.fetchall()
    for i in output:
        print(i)

elif a == 4:
    print("Enter the Name of the student: ")
    Name = input()
    sql = "delete from student where Name = %s"
    cursor.execute(sql, (Name,))
    connector.commit()
    print("Student Record Deleted")

elif a == 5:
    print("Enter 1. To Edit All Fields: ")
    print("Enter 2. To Edit Name: ")
    print("Enter 3. To Edit Department: ")
    print("Enter 4. To Edit Marks: ")
    b = int(input())
    if b == 1:
        print("Enter the id of the student: ")
        id = input()
        sql = "select * from student where id = %s"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        print(data)
        print("Enter the New Name of the student: ")
        Name = input()
        print("Enter the Department_Name: ")
        Department_Name = input()
        print("Enter the Mark_1: ")
        Mark_1 = int(input())
        print("Enter the Mark_2: ")
        Mark_2 = int(input())
        print("Enter the Mark_3: ")
        Mark_3 = int(input())

        total = Mark_1 + Mark_2 + Mark_3
        Average = total / 3
        if (Average > 90):
            Grade = "S"
        elif (Average > 81):
            Grade = "A"
        elif (Average > 71):
            Grade = "B"
        elif (Average > 61):
            Grade = "C"
        elif (Average > 56):
            Grade = "D"
        elif (Average > 50):
            Grade = "E"
        else:
            Grade = "U"
        sql = "Update student.student SET name=%s, depart=%s, mark1=%s, mark2=%s, mark3=%s, totalmark=%s, average=%s, " \
              "grade=%s WHERE id= %s "
        Val = (Name, Department_Name, Mark_1, Mark_2, Mark_3, total, Average, Grade, id,)
        cursor.execute(sql, Val)
        connector.commit()
        print("Student details Updated")
    if (b == 2):
        print("Enter the id of the student: ")
        id = input()
        sql = "select * from student where id = %s"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        print(data)
        print("Enter New Name: ")
        name = input()
        sql = "UPDATE student SET name= %s WHERE id= %s"
        value = (name, id)
        cursor.execute(sql, value)
        connector.commit()
        print("Name Updated Sucessfuly")
    if (b == 3):
        print("Enter the id of the student: ")
        id = input()
        sql = "select * from student where id = %s"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        print(data)
        print("Enter New depart: ")
        depart = input()
        sql = "UPDATE student SET depart= %s WHERE id= %s"
        value = (depart, id)
        cursor.execute(sql, value)
        connector.commit()
        print("Department Updated Sucessfuly")
    if (b == 4):
        print("Enter the id of the student: ")
        id = input()
        sql = "select * from student where id = %s"
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        print(data)
        print("Enter the Mark_1: ")
        Mark_1 = int(input())
        print("Enter the Mark_2: ")
        Mark_2 = int(input())
        print("Enter the Mark_3: ")
        Mark_3 = int(input())

        total = Mark_1 + Mark_2 + Mark_3
        Average = total / 3
        if (Average > 90):
            Grade = "S"
        elif (Average > 81):
            Grade = "A"
        elif (Average > 71):
            Grade = "B"
        elif (Average > 61):
            Grade = "C"
        elif (Average > 56):
            Grade = "D"
        elif (Average > 50):
            Grade = "E"
        else:
            Grade = "U"
        sql = "Update student.student SET mark1=%s, mark2=%s, mark3=%s, totalmark=%s, average=%s, grade=%s WHERE id= %s"
        Val = (Mark_1, Mark_2, Mark_3, total, Average, Grade, id,)
        cursor.execute(sql, Val)
        connector.commit()
        print("Student Mark details Updated")
    else:
        print("Thank you for connect")

elif (a == 6):
    connector.close()
    cursor.close()
    print("Exited in MySQL connection")

else:
    print("Thank you for connect")
