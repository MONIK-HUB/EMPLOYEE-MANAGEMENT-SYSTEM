import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
class table_op:
   musicdb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MONIK2000",
        database="musicperk"
    )
   def createconnection(self):
       self.musicdb = mysql.connector.connect(
           host="localhost",
           user="root",
           password="MONIK2000",
           database="musicperk"
       )
   def createtable(self):
       mycur=self.musicdb.cursor()
       mycur.execute("Show tables")
       myres = mycur.fetchall()
       print(myres)
       tname=str(input(" enter table name which is not in above list"))
       mycur.execute("CREATE TABLE IF NOT EXISTS %s(emp_id INT(11) ,emp_name VARCHAR(200), emp_age INT(11),salary INT(11),manager_id INT(20))"%tname)
       self.musicdb.commit()
   def queries(self,ch):
       mycur = self.musicdb.cursor()
       if(ch==1):
           mycur.execute("Show tables")
           myres = mycur.fetchall()
           print(myres)
           tname = str(input(" enter table name from above list"))
           mycur.execute("SELECT * FROM %s"%tname)
           myres=mycur.fetchall()
           for x in myres:
               print(x)
       elif(ch==2):
            mycur.execute("Show tables")
            myres = mycur.fetchall()
            print(myres)
            tname = str(input(" enter table name from above list"))
            eid=str(input('enter employee id'))
            name=str(input('enter name'))
            sal=str(input('enter salary'))
            age=str(input('enter age'))
            mid=str(input('manager id'))
            mycur.execute("INSERT INTO {} values (%s,%s,%s,%s,%s);".format(tname),(eid,name,age,sal,mid))
            self.musicdb.commit()
       elif(ch==3):
           mycur.execute("Show tables")
           myres = mycur.fetchall()
           print(myres)
           tname = str(input(" enter table name from above list"))
           eid = str(input('enter employee id'))
           mycur.execute("DELETE FROM {} WHERE emp_id=%s".format(tname),(eid,))
           self.musicdb.commit()
       elif(ch==4):
           mycur.execute("Show tables")
           myres = mycur.fetchall()
           print(myres)
           tname = str(input(" enter table name from above list"))
           df = pd.read_sql('SELECT *FROM {} '.format(tname), con=self.musicdb)
           count=int(0.1*len(df.index))
           print(df.nlargest(count,'salary'))
       elif(ch==5):
           mycur.execute("Show tables")
           myres = mycur.fetchall()
           print(myres)
           tname = str(input(" enter table name from above list"))
           df=pd.read_sql('SELECT * FROM  {} e1 where emp_id in (''select emp_id from {} e2 where e1.emp_age>e2.emp_age and e1.manager_id=e2.emp_id'')'.format(tname,tname),con=self.musicdb)
           print(df)
       elif(ch==6):
           mycur.execute("Show tables")
           myres = mycur.fetchall()
           print(myres)
           tname = str(input(" enter table name from above list"))
           df=pd.read_sql('select * from {}'.format(tname),con=self.musicdb,index_col='emp_id')
           print(df)
           df['salary'].plot(color='k', label='SALARY')
           plt.ylabel('SALARY', fontsize=15)
           plt.xlabel('EMPLOYEE ID', fontsize=15)
           plt.title('MUSICPERK INTERNSHIP TASK BY MONIK', fontsize=20)
           plt.show()
           plt.bar(df.index,df.salary, color='maroon',width=2)
           plt.ylabel('SALARY', fontsize=15)
           plt.xlabel('EMPLOYEE ID', fontsize=15)
           plt.title('MUSICPERK INTERNSHIP TASK BY MONIK', fontsize=20)
           plt.show()

class employees(table_op):
    def __init__(self):
     t=table_op()
     while True:
      print('--------menu----------'
        '\n 1.addemployee'
        '\n 2.plot salary graph'
        '\n 3.employees older than managers'
        '\n 4.display top 10 percentage highly paid employees'
        '\n 5.delete an employee record'
        '\n 6.create a new table'
        '\n 7.establish a connection'
           '\n 8.exit')
      ch=int(input('enter your choice'))

      if ch == 1:
       t.queries(2)
      elif ch == 2:
       t.queries(6)
      elif ch == 3:
       t.queries(5)
      elif ch == 4:
       t.queries(4)
      elif ch == 5:
       t.queries(3)
      elif ch == 6:
       t.createtable()
      elif ch == 7:
       t.createconnection()
      elif ch == 8:
        break
      else:
        print("\n enter correct option")
e=employees()

