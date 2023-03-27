import sqlite3
from tabulate import tabulate

con = sqlite3.Connection("Exp1.dp")

cursor = con.cursor()

Table = """CREATE TABLE if not exists Monthly_Exp
            (ID INTEGER NOT NULL PRIMARY KEY,
            Date DATE,
            Category VARCHAR(100),
            Amount FLOAT, 
            Remarks VARCHAR(100));"""

cursor.execute(Table)


def insert(Date, Category, Amount, Remarks):
    sql = "INSERT into Monthly_Exp (Date, Category, Amount, Remarks) values (?, ?, ?, ?)"
    data = (date, category, amount, remarks)
    cursor.execute(sql, data)
    con.commit()
    print("Date insert successfully")


def update(Date, Category, Amount, Remarks, id):
    sql = "Update Monthly_Exp set Date=?, Category=?, Amount=?, Remarks=? Where id=?"
    data_update = (date, category, amount, remarks, id)
    cursor.execute(sql, data_update)
    con.commit()
    print("Date update successfully")


def select():
    sql = "select ID, Date, Category, Amount, Remarks from Monthly_Exp"
    cursor.execute(sql)
    data_select = cursor.fetchall()
    print(tabulate(data_select ,headers=["ID", "Date", "Category", "Amount", "Remarks"]))


def Total():
    sql = "select total(Amount) from Monthly_Exp"
    cursor.execute(sql)
    con.commit()
    print("The total amount spend:")
    print(cursor.fetchone()[0])


def delete(id):
    sql = "delete from Monthly_Exp where id=?"
    data = (id)
    cursor.execute(sql, data)
    con.commit()
    print("Data deleted successfully")


while True:
    print("1.Insert the value")
    print("2.update the value")
    print("3.Total")
    print("4.To show the data..")
    print("5.To Delete the data..")
    print("6.Exit")
    choice = int(input("Enter the choice..?"))
    if choice == 1:
        date = input("Enter the Date(YYYY/MM/DD):")
        category = input("Enter the category:")
        amount = input("Enter the Amount:")
        remarks = input("Enter the Remark:")
        insert(date, category, amount, remarks)
    elif choice == 2:
        id = input("Enter the id: ")
        date = input("Enter the Date (YYYY/MM/DD):")
        category = input("Enter the category:")
        amount = input("Enter the Amount:")
        remarks = input("Enter the Remark:")
        update(date, category, amount, remarks, id)
    elif choice == 3:
        Total()
    elif choice == 4:
        select()
    elif choice == 5:
        id = input("Enter the id to delete..")
        delete(id)
    elif choice == 6:
        quit()
    else:
        print("Enter the valid number..!")
