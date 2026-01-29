# Tuple
#()
#(item1,item2,...)
#sequence of items as a collections
# in tuple you cannot add extra elements
s1=[1,5,8]
t1 = ("python", 10, 0.5, True, [1,2,3],(10,20,3),s1) #tuple
print(len(t1))
print(t1[-1])
print(t1[1:6:2])
print(type(t1))
print(t1[-1])
print(t1, type(t1))

fruits= ("mango", "orange", "apple", "banana")
print(fruits, type(fruits))
fruits= list(fruits)
print(fruits, type(fruits))
fruits.append("kiwi")
print(fruits, type(fruits))
