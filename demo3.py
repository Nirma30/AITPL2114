import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table emp_saniya(regno varchar(10),name varchar(20),salary varchar(6))")
def insert_table():
    c.execute("insert into emp_saniya values('AITPL2110','shaik saniya','12000')")
    c.execute("insert into emp_saniya values('AITPL2111','saniya','13000')")
    c.execute("insert into emp_saniya values('AITPL2112','Reeha','15000')")
    c.execute("insert into emp_saniya values('AITPL2113','Afiya','16000')")
    c.execute("insert into emp_saniya values('AITPL2114','sana','19000')")
    con.commit()
def select_table():
    c.execute('select * from emp_saniya')
    data=c.fetchall()
    for row in data:
        print(row)
def update_table():
    c.execute("update values into emp_saniya values('")

# create_table()
# insert_table()
select_table()
c.close()
con.close()