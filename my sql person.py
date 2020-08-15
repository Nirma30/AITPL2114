import mysql.connector
# from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141', database='db1', user='root', password='India12345')
c = con.cursor()


def create_table():
    c.execute("create table person_nirma(name varchar(10), dob varchar(20), address varchar(20), pannum varchar(10))")


def insert_table():
    c.execute("insert into person_nirma values('rajesh', '02 jun 1994', 'rajajinagar', '36849342')")
    c.execute("insert into person_nirma values('swetha', '31 may 1993', 'krpuram', '745357683')")
    c.execute("insert into person_nirma values('aasin', '15 feb 1998', 'marathahalli', '67344757')")
    c.execute("insert into person_nirma values('sagar', '25 nov 1995', 'whitefield', '56478596')")
    c.execute("insert into person_nirma values('riya', '09 jun 1994', 'tinfactory', '8674463758')")
    con.commit()


def select_table():
    c.execute('select * from person_nirma')
    data = c.fetchall()
    for row in data:
        print(row)


def update_table():
    c.execute('update person_nirma set pannum=2754389 where name="sagar" ')


def delete_table():
    c.execute('delete from person_nirma where name="aasin"')


create_table()
insert_table()
select_table()
update_table()
delete_table()
c.close()
con.close()
