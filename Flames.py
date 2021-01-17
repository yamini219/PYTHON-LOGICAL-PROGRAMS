name1=input("Enter the name1:").lower()
name2=input("Enter the name2:").lower()
name1=name1.replace(" ","")
name2=name2.replace(" ","")
for i in name1:
  for j in name2:
    if i==j:
      name1=name1.replace(i,"",1)
      name2=name2.replace(j,"",1)
      break
count=len(name1+name2)
print(count)
if count>0:
  list=["Friends","Lovers","Affection","Marriage","Enemies","Siblings"]
  while len(list)>1:
    c=count%len(list)
    index=c-1
    if index>=0:
      left=list[:index]
      right=list[index+1:]
      list=right+left
    else:
      list=list[:len(list)-1]
  print("Relationship is:",list[0])
else:
  print("Type different name")

