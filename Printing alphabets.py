num=int(input("Enter the number:"))
space=num-1
for i in range(num):
  for j in range(space-i):
    print(end=" ")
  for j in range(i+1):
    print(chr(98+j-1),end=" ")
  print("\r")
  
   