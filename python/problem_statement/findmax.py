
"""This function finds the maximum element in a list of integers.

def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num

            
    return max_element

print(find_max([1, 3, 5, 10, 9]))

"""


arr=[1,2,3,4,5,6,7,8,9]

arrlen=len(arr)

secondmax=int(arrlen-1)

def bsa(arr,target):
    low,high = 0,len(arr)-1
    while low <= high:
        mid =(low+high)//2
        if arr[mid] ==target:
            return mid
        elif arr[mid] < target:
            low = mid + 1   
        else:
            high =mid -1
    return -1

print(bsa(arr,arr[secondmax]))
