# lists are ordered collection of data items. they store multiple items in a single variable. list items are separated by commas and enclosed
list1 = ["apple", "banana", "mango", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(type(list1))
print(list1[0:7])
print(len(list1))
print(list1[-3])
list1.append("orange")
print(list1)
if 9 in list1:
  print("yes")
else:
  print("no")
# making list from user input
list2 = []
listitem = int(input("enter the number of items in list: "))
for i in range(listitem):
  a = input(f"enter the value of item {i+1} for list2: ")
  list2.append(a)
print("list2 is", list2)
marks = [2, 3, 4, 12, 13, 14, 15, 5, 6, 7, 8, 9, 10 , 11]
print(marks[1:8:2])
print(marks[:])
for i in marks:
  print(i)
print(marks.sort())
print(marks.reverse())
# list comprehension
l1=[x for x in range(10) if x%2==0]
print(l1)
l2=[x*x for x in range(10)]
print(l2)
# list methods
l=[9,2,4,6,6,9,0,9]
print(l.index(9))
l.append(4)
l.sort()
print(l[:])
print(l.index(9))
print(l.count(9))
l.sort(reverse=True)
# l.reverse()
print(l)
m=l.copy()
m[0]=10
m[5]=0
l.extend(m)
print(m)
print(l)
k=l+m
print(k)
