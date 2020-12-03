num=int(input("number:"))
space=num-1
for i in range(num):
  for j in range(space-i):
    print(end=" ")
  for k in range(i+1):
    print(i+1,end=" ")
  print("\r")
num=4
num1=6
for i in range(num):
  for j in range(i+1):
    print(end=" ")
  for k in range(num-i):
    print(num1+i,end=" ")
  print("\r")
    
  