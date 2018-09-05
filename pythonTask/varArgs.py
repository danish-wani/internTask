def func(*args):
     print(type(args))
     for index, value in enumerate(args):
             print(index,value)

func(2,3,4)
