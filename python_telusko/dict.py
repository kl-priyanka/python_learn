#dictionaries in python
num={1:'one', 5:'five', 2:'two', 'nine':9} #1 is key and 'one' is the value
print (num)
print(num['nine'])
print(num.get(1)) #get function is same as fetching the value normally using '[]' in the previous line
print(num.get(4)) #here, even though there is no key named '4' we did not get any error, instead it displays 'none' in the output
#print(num[4]) #but this way you will get an error message like (KeyError: 4)
print(num.get(1,'not found')) #here it prints 'one' instead of 'not found' because the value for the key '1' exists
print(num.get(4,'not found')) #it gives the value of 4 as 'not found' because the key '4' does not exist
print(num) #the key and value of '4' won't be reflected in the actual dictionary 'num'
num['nine']='thommidhi' #we can change the values of the dictionaries
print(num)

keys = [1,2,3]
values = ['one', 'two', 'three']
dictionary = dict(zip(keys,values)) #merges two lists into a dictionary
print(dictionary)
dictionary[4]='four' #assigns a new key and value
print(dictionary)
del dictionary[1] #deletes a key and value
print(dictionary)

#we can put lists and dictionaries in a single dictionary as shown below
newDict = {1:'one', 2:'two', 3:['three', 'moodu'], 4:{'chaar':'naalugu', 'quatro':'quatre'}} 
print(newDict)
print(newDict[1])
print(newDict[3])
print(newDict[3][0])
print(newDict[4])
print(newDict[4]['chaar'])
print(newDict[4]['quatro'])