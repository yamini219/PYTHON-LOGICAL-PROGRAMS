def insertionsort(list):
  for index in range(1,len(list)):
    current_element=list[index]
    pos=index
    while current_element<list[pos-1]and pos>0:
      list[pos]=list[pos-1]
      pos=pos-1
    list[pos]=current_element
list=[5,3,2,4,1,6,0,-2]
insertionsort(list)
print(list)
