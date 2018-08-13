def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b

fib(100)
print(fib)  #the value of the function name has a type recognized by the interpreter as a user-defined function.
f = fib     #value of a user-defined function assigned to fib

f(100)
