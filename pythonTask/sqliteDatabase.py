import sqlite3
import json
from classes import Employee
from classes import Student
# conn = sqlite3.connect(':memory:')		#creating a connection object			:memory:  creates on RAM used for quick testing
# c = conn.cursor()						#creating a cursor object which allows us to execute sql commands using its execute method

# c.execute('''CREATE TABLE employees (fname text,lname text,pay integer	)''')


def insert_emp(emp):
	with conn:			#context manager , implicitly saves or commits the changes
		print(c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp.fname,emp.lname,emp.pay)))


def update_pay(fname,lname,pay):
	with conn:
		c.execute("UPDATE employees SET pay = :pay WHERE fname = :fname and lname = :lname",{'pay':pay,'fname':fname,'lname':lname})


def remove_emp(fname,lname):
	with conn:
		c.execute("DELETE FROM employees WHERE fname = :fname and lname = :lname",{'fname':fname,'lname':lname})


#def get_emps(first,last):
#	c.execute('SELECT * FROM employees where fname = :first and lname = :last',{'first':first,'last':last})
#	print(c.fetchall())


# for students
def insert_std(std):
	with conn:			#context manager , implicitly saves or commits the changes
		c.execute("INSERT INTO students VALUES (?, ?, ?)",(std.name,std.age,std.address))


def update_stdAge(std,age):
	with conn:
		c.execute("UPDATE students SET age = :age WHERE name = :name  AND address = :add",{'age':age,'name':std.name,'add':std.address})


def remove_std(name,address):
	with conn:
		c.execute("DELETE FROM students WHERE name = :name and address = :add",{'name':name,'add':address})

def view_table(table_name):
    c.execute('SELECT name FROM {}'.format(table_name))
    records = c.fetchall()
    if len(records) == 0:
        print("Table is empty")
    else:
        print(c.fetchall())


def create_table(tableName,nameType):
    with conn:
        nametype = json.dumps(nameType)
        nametype = nametype.replace('}','')
        nametype = nametype.replace('{','')
        nametype = nametype.replace(':','')
        nametype = nametype.replace('"','')
        nametype = nametype.replace(':','')
        c.execute('''CREATE TABLE IF NOT EXISTS {0} ({1})'''.format(tableName,nametype))


def insert_table(tableName,data):
    with conn:
        dataStr = json.dumps(data)
        dataStr = dataStr.replace('[','')
        dataStr = dataStr.replace(']','')
        #dataStr = dataStr.replace('','')
        dataStr = dataStr.strip()
        print(dataStr)
        c.execute("INSERT INTO {0} VALUES ({1})".format(tableName,dataStr))
    



#def get_std(first,last):
#c.execute('SELECT * FROM employees where fname = :first and lname = :last',{'first':first,'last':last})
#print(c.fetchall())




dbname = "School.db"
print("")
print("Database name is {}".format(dbname))
conn = sqlite3.connect(dbname)		#creating a connection object			:memory:  creates on RAM used for quick testing
c = conn.cursor()						#creating a cursor object which allows us to execute sql commands using its execute method
#c.execute('''CREATE TABLE IF NOT EXISTS employees (fname text,lname text,pay integer)''')
#c.execute('''CREATE TABLE IF NOT EXISTS students (name text, age integer, address text)''')




data = []

data = str(input('Enter all the required details in order separated by a space:')).split(" ")

dataStr = json.dumps(data)

dataStr = dataStr.replace('"','')
dataStr = dataStr.replace('[','')
dataStr = dataStr.replace(']','')
dataStr = dataStr.strip()
print(dataStr)


c.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name")
tables = c.fetchall()
print("**List of the tables in the database {0} are: ".format(dbname) +"**")
for tb in tables:
    print("{}".format(tb))
choice = 1

#c.execute("SELECT * FROM pragma_table_info")
#print(c.fetchall())
#c.execute("SELECT typeof(fname) FROM employees")
#print(c.fetchall())



c.execute("SELECT sql FROM sqlite_master")
print(c.fetchall())
while choice != 0:
    choice = int(input('Enter\n 1 to Select the existing table \n 2 to Create a new table \n 3 to Clear a table \n 4 to Delete an existing table \n 5 to View all tables \n 0 to Exit: \n'))
    #print(type(choice))
    
    if choice == 1:
        table_name = str(input('Enter the name of the table: '))
        c.execute("SELECT * FROM {}".format(table_name))
        if len(c.fetchall()) == 0:
            print("Table is empty")
        #else:
            #print(c.fetchall())
        op = int(input('Enter \n 1 to Insert \n 2 to Update \n 3 to View the table:\n 4 to remove a record: '))
        #c.execute("SELECT sql FROM sqlite_master")
        #print(c.fetchall())
        if op == 1:
            if table_name == 'employees':
                fname, lname, pay = str(input('Enter firstname, lastname, & pay: ')).split(" ")
                #print(fname, lname,pay)
                emp = Employee(fname,lname,int(pay))
                insert_emp(emp)
         
                view_table(table_name)
                #c.execute("SELECT * FROM {}".format(table_name))
                #print(c.fetchall())

            if table_name == 'students':
                name, age, address = str(input('Enter name, age, & address: ')).split(" ")
                #print(name,age,address)
                std = Student(name,int(age),address)
                insert_std(std)
                
                view_table(table_name)
                #c.execute('SELECT * FROM {}'.format(table_name))
                #print(c.fetchall())
            else:
                data = []
                data = str(input('Enter all the required details in order separated by a space:')).split(" ")
                insert_table(table_name,data)    
        elif op == 2:
            if table_name == 'employees':
                fname, lname = str(input('Enter the first and last name of the employee: ')).split(" ")
                newpay = int(input('Enter the new pay amount for the {} {}'.format(fname,lname)))
                update_pay(fname,lname,newpay)
                view_table(table_name)
                #c.execute('SELECT * FROM {}'.format(table_name))
                #print(c.fetchall()) 
        
        elif op == 3:
            view_table(table_name)
            #c.execute('SELECT * FROM {}'.format(table_name))
            #print(c.fetchall()) 
        
        elif op == 4:
            if table_name == 'employees':
                fname, lname = str(input('Enter the first and last name of the employee: ')).split(" ")
                remove_emp(fname,lname)
                
            if table_name == 'students':
                name, address = str(input('Enter name, & address: ')).split(" ")
                remove_std(name,address)
                
            view_table(table_name)
        
        else:
            print('Invalid Choice')
        

    elif choice == 2:
        tableName = str(input('Enter the name of the new table: '))
        num = int(input("Enter number of columns: "))
        nameType = dict()
        for i in range(num):
            key, value = str(input('Enter name and type of the column: ')).split(" ")
            nameType[key] = value
            
            
            #nameType[x] = (y for x,y in input().split(" "))
        print(nameType)
        create_table(tableName,nameType)


    elif choice == 3:
        truncTab = str(input('Enter the name of the table you want to Clear: '))
        confirm = str(input("Are you sure you want to Clear the table? Y / N "))
        if confirm.lower() == 'y':
            c.execute("DELETE FROM {}".format(truncTab))
    elif choice == 4:
        delTab = str(input('Enter the name of the table you want to Delete: '))
        confirm = str(input("Are you sure you want to Delete the table? Y / N "))
        if confirm.lower() == 'y':
            c.execute("DROP TABLE {}".format(delTab))
    
    elif choice == 5:
        c.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name")
        tables = c.fetchall()
        print("**List of the tables in the database {0} are: ".format(dbname) +"**")
        for tb in tables:
            print("{}".format(tb))
    elif choice == 0:
        print('Signing off')
    else:
        print('Invalid Choice')


# c.execute('''CREATE TABLE employees (fname text,lname text,pay integer	)''')



#print('Enter firstname, lastname, & pay: ')
#fname = str(input('Enter first name: '))
#lname = str(input('Enter last name: '))
#pay = int(input('Enter pay: '))

#emp_10 = Employee(fname,lname,pay)
#emp_11 = Employee('Basit','Naqash',90000)

#insert_emp(emp_10)
#insert_emp(emp_11)
#get_emps('Basit','Naqash')




#print(sqlite3.version)
#print(sqlite3.PARSE_DECLTYPES)
# print(emp_10.email)
# c.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_10.fname,emp_10.lname,emp_10.pay))	# ? DB-api's parameter subst, passing parameters in tuple

# #another way of using plalceholders passing args as dictionary
# c.execute("INSERT INTO employees VALUES (:fname, :lname, :pay)",{'fname':emp_11.fname,'lname':emp_11.lname,'pay':emp_11.pay})	

# c.execute('SELECT * FROM employees where lname = :last',{'last':'wani'})
# print(c.fetchall())

# conn.commit()	#commit or save the changes
conn.close()

