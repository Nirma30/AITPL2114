import mysql.connector
# from mysql.connector import *
con = mysql.connector.connect(host='18.219.99.141', database='db1', user='root', password='India12345')
c = con.cursor()


def create_table():
    c.execute("create table product(prodid varchar(10), prodname varchar(20), prodprice varchar(10))")


def insert_table():
    c.execute("insert into product values('001', 'nestle','120')")
    c.execute("insert into product values('002', 'dove', '100')")
    c.execute("insert into product values('003', 'pantene', '250')")
    c.execute("insert into product values('004', 'dairymilk', '300')")
    c.execute("insert into product values('005', 'fair&lovely', '150')")
    con.commit()


def select_table():
    c.execute('select * from product')
    data = c.fetchall()
    for row in data:
        print(row)


def update_table():
    c.execute("update product set prodprice=650 where prodname='dairymilk' ")


def delete_table():
    c.execute("delete from product where prodid=001")


create_table()
insert_table()
update_table()
delete_table()
select_table()
c.close()
con.close()
