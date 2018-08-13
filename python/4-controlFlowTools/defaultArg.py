def f(a, L=[]):     #default value is evaluated only once
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))



def ff(a, Li=None):      #if we don't want the default to be shared between subsequent calls
    if Li is None:
        Li=[]
    Li.append(a)
    return Li


print(ff(1))
print(ff(2))
print(ff(3))


