#-----Linear Search-----#
#without function
arr = list(map(int , input("Enter spaced number:").split()))
ele = int(input("Enter a target element:"))
for i in arr:
  if i == ele:
    print(i)
else:
  print(0)
#with Function
  def find_element(arr, ele):
  
    for i in arr:
        if i == ele:
            return i
        else:
            return 0

arr = list(map(int, input("Enter spaced numbers: ").split())) 
ele = int(input("Enter a target element: "))
find_element(arr, ele)

#----------------------------------------------------------------------------------------#

#-----Binary Search-----#

#without function 
arr = list(map(int , input("Enter spaced number:").split()))
ele = int(input("Enter a target element:"))
low = 0
high = len(arr)-1
while low <= high:
  mid = (low+high)//2 # (left + (high - low ))//2
  if arr[mid] == ele:
    print(mid)
    break 
  elif arr[mid] < ele:
    low = mid+1 
  else:
    high = mid -1 


  #with function
  
  def binary_search(arr, ele):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            low = mid+1 
        else:
            high = mid -1 
    return 0
arr = list(map(int, input("Enter spaced numbers: ").split()))
ele = int(input("Enter a target element: "))
print(binary_search(arr, ele))

#------------------------------------------------------------------------------------#

  