
class Complex:
    '''trying my hands on python classes'''
    #i = 12345
    #def f():
        #return 'Hello World!'
    def __init__(self,real,imag):
        self.r = real
        self.i = imag

#print(Complex.r)
#print(Complex.i)
print(Complex.__doc__)

'''Class instantiation'''
x = Complex(3,5)

print(x.r)
print(x.i)
x.counter = 1
print(x.counter)    #data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.
#del x.counter       #deletes an attribute
#print(x.counter)

