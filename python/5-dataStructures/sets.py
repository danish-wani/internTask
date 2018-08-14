
basket = {'orange','banana','apple','mango'}
print(basket)

emptyBasket = {}    #creates an empty dictionary instead of empty set
emptyBasket = set() #correct way 

print('orange' in basket)      #fast membership testing

# set operations

fname = set('danish')
lname = set('wani')
print('first name: ',fname)
print('last name: ',lname)
print('letters in firstname but not in last name: ',fname - lname)    # letters in fname but not in lname
print('letters in firstname or lastname or both: ',fname | lname)       #letters in fname or lname or both
print('letters in both firstname and lastname: ',fname & lname)        #letters in both fname and lname
print('letters in firstname or lastname but not both: ',fname ^ lname)   #letters in firstname or lastname but not both

