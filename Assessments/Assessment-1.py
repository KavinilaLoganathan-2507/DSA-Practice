
# ---------------Assessment 1-----------------#

#To count the number of swaps in bubble sort

N = int(input("Enter the number of elements: ").strip())
A = list(map(int, input("Enter the elements: ").strip().split()))

swap_count = 0

for i in range(N):
    for j in range(0, N - i - 1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            swap_count += 1
            
print(swap_count)

#To find number of passes 


N = int(input("Enter the number of elements: ").strip())
A = list(map(int, input("Enter the elements: ").strip().split()))

passes = 0

for i in range(N - 1):
    for j in range(N - 1 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
    passes += 1

print(passes)



#To find the index of an element in an array - Linear Search

N = int(input("Enter the number of elements: ").strip())


arr = list(map(int, input("Enter the elements: ").strip().split()))


X = int(input())


result = -1

for i in range(N):
    if arr[i] == X:
        result = i 
        break       


print(result)


