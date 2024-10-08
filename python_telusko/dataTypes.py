#none, numeric, list, tuple, set, string, range, dictionary are the datatypes
#none : when a variable is not assigned with any value; similar to null
#numeric : int, float, complex, bool
#complex : 1+5j (1 is real part and 5 is imaginary part)

#typecasting
a=5.6
b=int(a)
print(a,type(a))
print(b,type(b))
c = 1+5j
print(c,type(c))
d = complex(a,b)
print(d,type(d))

#bool represents True(1) or False(0)

print(a<b)
print(a>b)
print(int(True),int(False))

#List, tuple, set, string, range come under 'Sequence'
lst=[1,2,3]
tup = (4,5,6)
s = {7,8,9}
r = (range(10))
print(r)
l2 = list(range(10))
print(l2)
l3 = list(range(0,10,2))
print(l3)

#dictionary : usually every value has an index but here every value has a key

d1 = {1:'one', 2:'two', 3:'three', 'four':4}
print(d1.keys())
print(d1.values())
print(d1['four'])
print(d1.get(3))
print(d1.get('three')) #we get 'None' because there is no such key