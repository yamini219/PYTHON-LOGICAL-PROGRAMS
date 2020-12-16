print("Enter 1 for +"
      "Enter 2 for -"
      "Enter 3 for *"
      "Enter 4 for /")
N=int(input("Enter your choice:"))
value1=int(input("Enter the first value:"))
value2=int(input("Enter the second value:"))
if N==1:
  print("The result is:",value1+ value2)
elif N==2:
  print("The result is:",value1-value2)
elif N==3:
  print("The result is:",value1* value2)
elif N==4:
  print("The result is:",value1/ value2)

