number=int(input("enter the number:"))
for i in range(0,number):
  number=i
  result=0
  n=len(str(i))
  while(i!=0):
    digit=i%10
    result=result+digit**n
    i=i//10
  if number==result:
    print(number," is armstrong number")
  