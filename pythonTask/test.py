class Employee:
	roi = 1.04
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+"."+last+"@company.com"
	
	def raise_amount(self):
		return 	self.pay * Employee.roi

	def full_name(self):
		return  self.first+" "+self.last

	def __add__(self,other):
		if isinstance(other,Employee):
			return self.pay + other.pay	
		return NotImplemented


class Project:
	pass

class Developer(Employee):

	def __init__(self,first,last,pay,prog_lang):
		Employee.__init__(self,first,last,pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self,first,last,pay,emp_list=None):
		Employee.__init__(self,first,last,pay)
		
		if emp_list is None:
			self.emp_list = []
		else:	
			self.emp_list = emp_list

		def add_emp(self,emp):
			if emp not in emp_list:
				emp_list.append(emp)

		def rem_emp(self,emp):
			if emp not in emp_list:
				emp_list.remove(emp)



emp_1 = Employee('danish','wani',50000)
emp_2 = Employee('abdul','basit',70000)
dev_1 = Developer('danish','wani',60000,'python')
pro_1 = Project()
man_1 = Manager('yaseen','dar',100000,'dev_1')
print(emp_1 + dev_1)
print(isinstance(dev_1,Developer))





'''print(dev_1.email)
print(dev_1.prog_lang)

print(man_1.email)
print("employess under "+man_1.full_name()+" are "+man_1.emp_list)
#print(issubclass(Manager,Employee))
print(help(dev_1))
print(help(man_1))

#method overloading is not supported by Python
def func(a,b,c):
	return a + b + c

def func(a,b):
	#return a + b

print(func(1,2,3))
print(func(1,2))'''