"""
second largest elements in the array
"""
#solution
#solution
arr = [12 , 36, 24, 23, 29]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest:
        second_largest = arr[i]
print("the second largest element in the array:", second_largest)


"""
the third largest elements in the array
"""
#solution

