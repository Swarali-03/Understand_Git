"""s1 = "python is cool"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version= "3.13.3"
print(language + version)
#print("Python" - language[0])
print(s1 * 3)
"""

# Membership operations on string
# in
s1 = "Python is fun"
print("Python" in s1)
print("i" in s1)
print("z" in s1)
print("java" in s1)

print()
#not in
print("Python" not in s1)
print("i" not in s1)
print("z"not in s1)
print("java" not in s1)

print()
print("\n"*3)

# Comparison os Strings
print("python"=="python")
print("python "=="python")

print("\n"*4)
s1= "python "
s2= s1.strip() #removes trailing or initial spaces in strings
print(s2)
print(s2=="python")
print(s1.strip()=="python")


print("\n"*4)
#replace()
s1= "We r learning python"
print(s1)
print(s1.replace("python","Java"))
print(s1)
print(s1.replace("e","E"))
print(s1.replace("e","E", count=1))