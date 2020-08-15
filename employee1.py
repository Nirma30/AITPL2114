import mysql.connector
# from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141', database='db1', user='root', password='India12345')
#con = mysql.connector.connect(host='localhost', database='db1', user='root', password='mithalal')
c = con.cursor()


def create_table():
    c.execute("create table nirma_employee(empid varchar(10), empname varchar(20), salary varchar(8))")


def insert_table():
    c.execute("insert into nirma_employee values('1001', 'raj', '20000')")
    c.execute("insert into nirma_employee values('1002', 'swathi', '25000')")
    c.execute("insert into nirma_employee values('1003', 'akash', '12000')")
    c.execute("insert into nirma_employee values('1004', 'simran', '22000')")
    c.execute("insert into nirma_employee values('1005', 'rahul', '200000')")
    con.commit()


def select_table():
    c.execute('select * from nirma_employee')
    data = c.fetchall()
    for row in data:
        print(row)


def update_table():
    c.execute("update nirma_employee set salary='15000' where empid='1003'")
    con.commit()


def delete_table():
    c.execute("delete from nirma_employee where empid='1005'")
    con.commit()


create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()
