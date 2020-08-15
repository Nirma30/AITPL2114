import mysql.connector
# from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141', database='db1', user='root', password='India12345')
c = con.cursor()


def create_table():
    c.execute("create table nirma(regno varchar(10), name varchar(20))")


def insert_table():
    c.execute("insert into student values('ATIPL2004', 'nirma')")
    con.commit()


def select_table():
    c.execute('select * from student')
    data = c.fetchall()
    for row in data:
        print(row)


create_table()
insert_table()
select_table()
c.close()
con.close()
