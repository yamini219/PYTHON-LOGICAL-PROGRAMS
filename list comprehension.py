list1=[]
for x in range(1,6):
  list1.append(x**2)
print(list1)
#list comprehension
list1=[x**2 for x in range(1,6)]
print(list1)
list2=[x**2 for x in range(5,0,-1)]
print(list2)
list3=[x if x<=5 else x+1 for x in range(1,11)]
print(list3)
list4=[x for x in range(1,11) if x%2==0]
print(list4)
list5=[x for x in range(1,6)]
print(list5*2)