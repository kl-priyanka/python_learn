list = [1,2,3,4] #a list is similar (but not the same) to an array in C or C++ languages 
print(list)
print(list[0])
#print(list[55]) #it displays error
print(list[-1])
print(list[:2])
print(list[2:])
print(list[:])
values = [1.5, 'bruh', 55]
print(values)
listOfLists = [list, values]
print(listOfLists)
list.append(5)
print(list)
#print(values.count(1))
list.insert(2,55)
print(list)
list.remove(5)
print(list)
list.pop()
print(list)
list.pop(1)
print(list)
list.append(88)
list.append(99)
print(list)
del list[4:]
print(list)
list.extend([111,222,333,444])
print(list)
print(min(list))
print(max(list))
print(sum(list))
list[7]=44
print(list)