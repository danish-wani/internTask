students={'qais':3,'basit':18,'danish':29 }
print(students)

students['afiq']=55
list(students)
print(sorted(students))         #sorted

print('danish' in students)     # in keyword to check the presence of any key
print('owais' not in students)  # not in keyword to check the absence of any key

# dict() constructor builds dictionaries directly from sequences of key-value pairs:

faculty=dict([('muheet',1),('chachoo',2),('jp',3),('sajid',4)])
print(faculty)

#dictionary comprehensions

squares={x:x**2 for x in range(10)}
print(squares)



