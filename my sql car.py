import mysql.connector
# from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141', database='db1', user='root', password='India12345')
c = con.cursor()


def create_table():
    c.execute("create table car_nirma(modelnum varchar(10), carname varchar(20), price varchar(10))")


def insert_table():
    c.execute("insert into car_nirma values('1001', 'ford','120000')")
    c.execute("insert into car_nirma values('1002', 'volkswagen', '400000')")
    c.execute("insert into car_nirma values('1003', 'bmw', '2000000')")
    c.execute("insert into car_nirma values('1004', 'jaguar', '3000000')")
    c.execute("insert into car_nirma values('1005', 'audi', '50000000')")
    con.commit()


def select_table():
    c.execute('select * from car_nirma')
    data = c.fetchall()
    for row in data:
        print(row)


def update_table():
    c.execute('update car_nirma set price=300000 where modelnum=1004 ')


def delete_table():
    c.execute("delete from car_nirma where carname='bmw'")


create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()
