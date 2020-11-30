num=int(input("Enter the number:"))
space=num-1
for i in range(num):
  for j in range(space-i):
    print(end=" ")
  for k in range(i+1):
    print("*",end=" ")
  print("\r")