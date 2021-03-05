from array import *
arr=array('i',[])
n=int(input("Enter the size of array "))
for i in range(n):
  x=int(input("Enter the values of array "))
  arr.append(x)
print(arr)
value=int(input("Enter the value you want "))
isPresent=bool(False);
for e in arr:
  if e==value:
    isPresent=True;
    break;

if (isPresent):
  print("Is present in the array")
else:
  print("Is not present in the array")
