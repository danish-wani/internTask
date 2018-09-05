class Employee:
	'''Employee class '''
	raise_amount = 1.04				#class variables shared among all instances of the class

	#regular methods  automatically passes instance and we callthat self
	def __init__(self,fname,lname,pay):
		self.fname = fname
		self.lname = lname
		self.email = self.fname+"."+self.lname+"@company.com"
		self.pay = pay

	def full_name(self):												
		return '{} {}'.format(self.fname.upper(),self.lname.upper())

	def apply_raise(self):
		self.pay = self.pay * self.raise_amount

	#class methods automatically passes class and we call that cls

	@classmethod	#decorator
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount	

	@classmethod						#classmethod used as an alternate constructor
	def fromEmployee(cls,fname,lname,pay):
		#fname, lname, pay = emp_str.split('-')
		return cls(fname,lname,pay)

	@staticmethod	#if we don't have to access the class or instance within the definition. They don't automatically take any argument.
	def workday(day):
		if day.weekday() ==  5 or day.weekday() ==  6:
			return False
		return True

	# iterator	__iter__(): returns an iterable object			__next__(): method of the returned iterable object
	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		
		self.index = self.index - 1
		return self.email[self.index]	


	# generators

	def rev(self,data):
		for index in range(len(data)-1,-1,-1):
			yield data[index]	


class Student:

	def __init__(self,name,age,address):
		self.name = name
		self.age = age
		self.address = address

if __name__ == '__main__':
	emp_1 = Employee('Danish','Wani',50000)
	emp_2 = Employee('Qais','Qadri',70000)
	emp_1.friend = "Abdul Basit"	#instance variable unique to each instnace

	# it = iter(emp_1.email)
	# print(next(it))

	# for i in emp_1.rev(emp_1.lname):
		# print(i)
	itr = emp_1.rev(emp_1.lname)
	print(next(itr))
	print(next(itr))
	print(next(itr))
	print(next(itr))
	print(emp_1.full_name())
	# print(emp_1.email)
	# print(emp_1.pay)

	Employee.set_raise_amount(1.06)

	#emp_1.raise_amount = 1.05
	# print(emp_1.apply_raise())
	# print(emp_1.pay)
	print(Employee.raise_amount)

	#empstr = 'owais-drabu-75000'
	emp_4 = Employee.fromEmployee('owais','drabu',75000)
	print(emp_4.full_name())

	import datetime				

	my_date = datetime.date(2018,9,1)

	print(Employee.workday(my_date))		#check whether the specified date is a working day

	# print('Employee1 namespace= ',emp_1.__dict__)		#namespace of emp_1 instnace

	# print(emp_1.__dict__['email'])
	# print(Employee.__dict__)
	# del Employee.set_raise_amount
	# print(Employee.__dict__)
	# emp_3 = Employee('Basit',"Naqash",80000)
	# print(Employee.full_name(emp_3))
	# print(Employee.full_name)
	# print(emp_1.full_name)
