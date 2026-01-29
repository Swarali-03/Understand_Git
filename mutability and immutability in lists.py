#lists are mutable
#tuples and strings are immutable

s1= "python is fun"
s2=s1.replace("python","java")
print(s1) ##see in o/p original string is not changed
print(s2)

"""t1=("mango", "banana","apple")
t2=t1.append("kiwi")
print(t1)### wont work in tuples
"""

l1=["mango", "banana","apple"]
l2=l1.append("kiwi")
print(l1) ##see in o/p original list is changed
print(l2)

l1[-1] = "orange"
print(l1)

s1="python is fun"
print(s1)
print(s1[0])
s1[0]= 'b' ##this wont work, since its a string, hence immutable

