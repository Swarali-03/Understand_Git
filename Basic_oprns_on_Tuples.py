"""
concatenation, repetition, membership
count, index
"""
#concatenation
student_details1= (100, "john")
student_details2= (78,98,85.5)
student_details= student_details1 + student_details2
print(student_details)
t1=("class5" , 5000)
print(t1*3)
# Membership
print(91 in student_details2)
print(91 not in student_details2)
#count
print(t1.count("class5"))
#index
print(t1.index("class5")) # number in sequence
t2=(0,2,1,4,7,1,6)
print(t2.index(1))
#min max and sum
print(min(t2))
print(max(t2))
print(sum(t2))


