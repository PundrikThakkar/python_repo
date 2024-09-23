import sqlite3
from employee import Employee

conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute('''CREATE TABLE employees(
            first text,
            last text,
            pay integer)''')

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})

def get_emp_by_name(lastname):
    with conn:
        c.execute("SELECT * FROM employees WHERE last=:last",{'last':lastname})

    return c.fetchall()

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first=:first AND last=:last",{'first':emp.first,'last':emp.last})

def update_pay(emp,pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE first=:first and last=:last",{'first':emp.first,'last':emp.last,'pay':pay})


emp1=Employee('John','Deo',50000)
emp2=Employee('Jane','Deo',60000)


insert_emp(emp1)
insert_emp(emp2)

update_pay(emp1,70000)
emp=get_emp_by_name('Deo')
print(emp)

remove_emp(emp2)
print(get_emp_by_name('Deo'))


conn.close()