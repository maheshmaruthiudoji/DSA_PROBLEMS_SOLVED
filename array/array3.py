"""
Find the largest elements in the array
"""
#solution
arr = [12 , 36, 24, 23, 23]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
        print("the largest element in the array:", largest)