def Binarysearch(list,target):
  left=0
  right=len(list)-1
  found=False
  while left<=right and not found:
    mid=(left+right)//2
    if target==list[mid]:
      found=True
    elif target<list[mid]:
      right=mid-1
    else:
      left=mid+1
  if found==True:
    print("Target is found")
  else:
    print("Target is not found")
list=[2,4,5,-2,11,43,-10]
list.sort()
print(list)
target=int(input("Enter the target:"))
Binarysearch(list,target)
