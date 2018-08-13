def packing(*arg,**keyword):        # *arg is a tuple that holds all the pos args, **keyword is a dictionary that holds all the keyword args
    for ar in arg:
        print (ar)

    for key in keyword:
        print(key,":",keyword[key])


packing("university","of","kashmir",department="computer science",name="danish wani",year="3rd")



#unpacking argument lists

def unpackPosArg(name,year,age):
    print(name," ",year," ",age)

arg=['danish','3rd',25]
unpackPosArg(*arg)                  # call with arguments unpacked from a list


def unpackKeywordArg(name='qais',year='',age=24):
    print(name,' ', year,' ',age)


kwarg={"name":"danish","year":"3rd","age":25}

unpackKeywordArg(**kwarg)
