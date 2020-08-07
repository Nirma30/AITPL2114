import sqlite3
con = sqlite3.connect('db.db')
c = con.cursor()

c.execute('create table emp(empid text,empname text)')
con.commit()
c.execute("insert into emp values('1001','raj')")
c.execute("insert into emp values('1002','anu')")
c.execute('select * from emp')
data = c.fetchall()
print(data)
