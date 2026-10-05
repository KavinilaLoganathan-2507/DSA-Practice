#Ascending order
numbers = list(map(int, input("Enter spaced numbers: ").split()))
numbers.sort()
print("Sorted numbers:", numbers)
#Descending order
numbers = list(map(int, input("Enter spaced numbers: ").split()))
numbers.sort(reverse=True)
print("Sorted numbers:", numbers)

#Sorted:
#ascending order
numbers = list(map(int, input("Enter spaced numbers: ").split()))
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers) # Will print new list not existing list .

#descending order
numbers = list(map(int, input("Enter spaced numbers: ").split()))
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted numbers:", sorted_numbers) # Will print new list not existing list .

#tuple:

user_tuple = tuple(input("Enter space-separated values: ").split())
user_tuple = tuple(sorted(user_tuple))
print("Sorted tuple:", user_tuple)

#If with mixed data types, you can use the key parameter to specify a custom sorting function. For example, if you have a list of strings and you want to sort them by their lengths, you can do the following:

items = [("apple", 3), ("banana", 1), ("cherry", 2)
]

def sort(items):
    return items[1]

items.sort(key=sort)  #items.sort(key=sort) #no positional arggument 
print(items)

#Lamda function:
items.sort(key=lambda items: items[1]) # parameters :expression
print(items)

#sorted(iterable , key , reverse)

#----------------------------------------------------------#

#Bubble sort
#without function 
arr = list(map(int , input("Enter spaced number:").split()))
size = len(arr) -1
for i in arr:
  for j in range(0,size):
    if arr[j] > arr[j+1]:
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
print(arr)


#with function 
def bubble_sort(arr):
    size = len(arr) - 1

    for i in range(len(arr)):
        for j in range(0, size - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


arr = list(map(int, input("Enter spaced numbers: ").split()))
print(bubble_sort(arr))

#---------------------------------------------------------------------#

#Selection sort 
#without function
arr = list(map(int, input("Enter numbers: ").split()))

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print("Sorted array:", arr)

#with function

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = list(map(int, input("Enter spaced numbers: ").split()))
print(selection_sort(arr))

#--------------------------------------------------------------------#

#Insertion sort

#with function 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#withpout function
arr = list(map(int, input("Enter numbers: ").split()))

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    for j in range(i - 1, -1, -1):
        if arr[j] > key:
            arr[j + 1] = arr[j]
        else:
            break

    arr[j + 1] = key

print("Sorted array:", arr)

#---------------------------------------------------------------------#
