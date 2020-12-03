num=int(input("number:"))
space=num-1
for i in range(num):
  for j in range(space-i):
    print(end=" ")
  for k in range(i+1):
    print("*",end=" ")
  print("\r")
num=num-1
num1=num+1
for i in range(num):
  for j in range(i+1):
    print(end=" ")
  for k in range(num-i):
    print("*",end=" ")
  print("\r")
    
