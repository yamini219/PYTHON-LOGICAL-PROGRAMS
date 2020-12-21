def bubblesort(list):
  for i in range(0,len(list)-1):
    for i in range(0,len(list)-1):
      if list[i]>list[i+1]:
        temp=list[i+1]
        list[i+1]=list[i]
        list[i]=temp
list=[0,22,-1,3,6,19,-4]
bubblesort(list)
print("The sorted list is",list)
