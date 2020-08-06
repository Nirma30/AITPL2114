import sqlite3
con = sqlite3.connect('db4.db')
c = con.cursor()

c.execute('create table student(rollno text primary key,sname text)')
c.execute("insert into student values('1001','raj')")
c.execute("insert into student values('1002','anu')")
c.execute("insert into student values('1003','anusha')")
c.execute("insert into student values('1004','seema')")
c.execute("insert into student values('1005','joy')")
c.execute('select * from student')
data = c.fetchall()
print(data)
c.execute('create table marks(sub1 text,sub2 text,sub3 text)')
c.execute("insert into marks values('95','88','85')")
c.execute("insert into marks values('85','80','83')")
c.execute("insert into marks values('95','94','100')")
c.execute("insert into marks values('64','73','85')")
c.execute("insert into marks values('90','84','89')")
con.commit()
c.execute('select * from marks')
data = c.fetchall()
print(data)
c.close()
con.close()
