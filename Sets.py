# #sets are non-sequential collection items, i.e we cannot have indexing in sets
# # , separated elements enclosed within {}
#
# set1={10,"python", 2.5}
# print(set1)
# print(type(set1))
# print(len(set1))
#
# #we can have a duplicate elements in lists and tuples, but we cannot have it in a set.
# l1=[10,20,10,30,40,10]
# print(l1, type(l1), len(l1))
# print(l1.count(10))
# t1=(10,20,10,30,40,10)
# print(t1, type(t1), len(t1))
# s1={10,20,10,30,40,10}
# print(s1, type(s1), len(s1))
#
# print("/n"*2)
# # Basic operations on sets
# nums1={1,3,2,0,-1,}
# #membership operators in sets
# print(1 in nums1)
#         # #concatenation in sets
#         # nums2={2,3,5,6}
#         # print(nums1 + nums2)
#         # #repetition
        # print(nums2 *3)
Weekdays= ("mon", "tues", "wed", "thur", "fri", "sat", "sun")#tuple
weekdays= set(Weekdays) # converting into sets
print(weekdays)

##mutablity in sets
weekdays.add("mango")  ## adding elems in sets
print(weekdays)

weekdays.remove("mango")
print(weekdays)

weekdays.discard("mango") # using discard wont gives an error even if the element is not present
print(weekdays)

## Union. intersection and difference in sets
student1 = {"english", "maths", "cs", "statistics"}
student2= {"english", "biology", "chem", "statistics"}

common_subjects= student1.intersection(student2)
print(common_subjects)
all_subjects= student1.union(student2)
print(all_subjects)
remaining_subjects= student1.difference(student2)
print(remaining_subjects)

## Frozen sets
s1= {1,2,3,4}
s1.add(-1)
print(s1)
#frozen sets are immutable sets
fs1 = frozenset({1,2,3,4})
print(fs1, type(fs1))
fs2= frozenset({10,2,30,4})
print(fs2, type(fs2))
print(fs2.isdisjoint(fs1))
print(fs2.union(fs1))
print(fs2.difference(fs1))
print(fs2.intersection(fs1))
print(fs2.symmetric_difference(fs1))
print(fs2.union(fs1))
print(fs2.difference(fs1))
print(fs2.intersection(fs1))







