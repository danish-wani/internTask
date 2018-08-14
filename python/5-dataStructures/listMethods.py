# list methods

fruits=['orange','banana','pear','kiwi','apple','mango','banana','melon']
fruits.append('grape')          #list.append() method adds element to the end of the list.
#fruits[len(fruits):]=['grape']
print('after append',fruits)


fastfood=['pizza','burger','roll','popcorn','shwarma']
print(fastfood)

food=[]

food.extend(fruits)         #list.extend(iterable) extend the list by appending all the items from the iterable.
food.extend(fastfood)
print('after extend method',food)


food.insert(len(food),'momos')  # list.insert(index,item) item to be placed before specified index
print('inserted momos before len(food)',food)


food.remove('banana')       #removes the first item from the list whose value is equal to specified item, raises ValueError if item not found
print('after removing the first occurence of banana',food)



food.pop()                  #removes the item at the given position in the list,and return it. If no index is specified it removes the last item in the list.
print('popped last item from list as no index was provided',food)


FOOD=food.copy()
print(FOOD)


FOOD.clear()                #list.clear() method as the name suggests is used to clear the list.
print('cleared list',FOOD)


print(food.index('kiwi'))               # returns zero based index in the list of th first item whose value is specified in the argument.


print('number of food items ',food.count('pizza'))                 #returns the number of times specified item appears in th list



food.reverse()                      #reverse the elements of the list in place
print('reversed the food list',food)



food.sort(key=lambda x: len(x))             #list.sort(key=None, reverse=False), sort the items of the list
print(food)
