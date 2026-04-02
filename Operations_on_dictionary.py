"""
marks={"Maths": 80.5, "English": 76.0, "Phy": 80}
print(marks)
print(marks["Maths"])
print(marks["English"])
print("\n")
#get()
print(marks.get("English"))
print(marks.get("Chem"))## even if not present,you'll get none
#print(marks["Chem"]) ## you'll get error

marks["Chem"]=80
print(marks)

emp1={'id': 1, 'name': 'john', 'salary': 100}
print(emp1)
print(emp1['salary'])
print(emp1.get("phone"))
print(emp1.keys())
print(emp1.values())
print(emp1.get("phone", 8329643526))
emp1['phone']= 8329643526
print(emp1)
print(emp1.items())
print(emp1.popitem())

# membership operator
print(1 in emp1)
print('id' in emp1)

emp1.update(marks)
print("emp1 is",emp1)

emp1.pop('name')
print("emp1 is",emp1)
#keys cannot be duplicated in a dictionary
"""
