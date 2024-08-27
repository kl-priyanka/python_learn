vari = 7
#id() to get the address of a variable
print(id(vari)) #140720377103080
name = 'Priyanka'
print(id(name)) #3006928534256
print("---------------------------------")
a = 10
b = a
print(id(a)) #140720377103176
print(id(b)) #140720377103176
print(id(10)) #140720377103176
print("---------------------------------")
#both a and b point to the variable a itself
#in python if two variables have the same data, it points to one variable only which is why python is memory efficient
c = 17
d = 17
print(id(c)) #140720377103400
print(id(d)) #140720377103400
print(id(17)) #140720377103400
print("---------------------------------")
#it points to the same variable (here c) even though we assign 7 to each c and d separately
c = 8
print(id(c)) #140720377103112
# here the address of c changes because its value has changed. but d still points to the previous address only. 
# Only c address will be changed because another memory location is assigned to store the new value of c
print(id(d)) #140720377103400
print(id(17)) #140720377103400
print(id(8)) #140720377103112
print("---------------------------------")
a = 19
print(id(a)) #140720377103464
print(id(b)) #140720377103176
#even though b = a, the value/address of b will not be changed to a
print("---------------------------------")
b = 100
print(id(b)) #140720377106056
print(id(10)) #140720377103176
#10 is not referenced by any variable so it will be ready for garbage collection later
print("---------------------------------")
#In python we cannot make any variable as constant but we can show that the variable is a constant by giving the variable name in all capitals
PI = 3.14 #we can change the value if we want but when a variable is in all capitals, it means that the programmer is intending to say that the variable is a constant and do not change it
print(type(PI)) #'float' datatype
print(type(a)) #'int' datatype
print(type('hello')) #'str' datatype