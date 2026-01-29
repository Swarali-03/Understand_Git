# name="John"
# age=20
# percent= 85
#
# student= [name,age,percent]
# print(student)
# print(type(student))
#
# days_of_week= ["mon","tue","wed","thurs","fri","sat","sun"]
# print(days_of_week[0])
# print(f"last day of the week is{days_of_week[-1]}")
# print(len(days_of_week))

##extend()
#remove()
#pop()
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
fruits.extend(["strawberry", "grapes"])
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.remove("strawberry")
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)