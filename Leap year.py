year=int(input("Enter the year:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print(year,"leap year")
    else:
      print(year,"not a leap year")
  else:
    print(year,"leap year")
else:
  print(year,"not a leap year")
