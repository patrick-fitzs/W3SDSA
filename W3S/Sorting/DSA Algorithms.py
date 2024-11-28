# find the min i na n arrau

def findMin(x):
    minvalue = x[0]
    for i in x:
        if i < minvalue:
            minvalue = i
    return minvalue
x = [34,5678,234,76,4]
print(f"max in array: {findMin(x)}")

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
## 0.1.1.2.3.5.8
print(f"6th number in fibo sequence = {fibo(6)}")

print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return
print()
print("first 19 numbers in fibonacci sequence")
fibonacci(1,0)

print("##########  bubble sort algo  ##########")
arr = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Before iteration :       {arr}")
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"Array after iteration {i+1}: {arr}")
bubbleSort(arr)

print("sorted array", arr)

print("\n##########  Selection sort algo  ##########\n")
arr1 = [77, 74, 25, 82, 32, 91, 21, 9]
print(f"Before iteration{arr1}")


def selectionSort(arr1):
    n = len(arr1)
    for i in range(n):
        # Find the index of the minimum element
        min_index = i
        for j in range(i + 1, n):
            if arr1[j] < arr1[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr1[i], arr1[min_index] = arr1[min_index], arr1[i]
        # Print the array after each iteration
        print(f"Iteration {i + 1}: {arr1}")

# Example usage

selectionSort(arr1)
print("Final sorted array:", arr1)

print("\n##########  Insertion sort algo  ##########\n")
arr3 = [77, 74, 25, 82, 32, 91, 21, 9]
print(f"Before iteration : {arr3}")

def insertionSort(arr3):
    n = len(arr3)
    for i in range(1, n):
        current_value = arr3[i]
        j = i - 1
        # Shift elements of arr2[0..i-1] that are greater than current_value
        while j >= 0 and arr3[j] > current_value:
            arr3[j + 1] = arr3[j]
            j -= 1
        arr3[j + 1] = current_value
        # Print the array after each iteration
        print(f"Iteration {i}: {arr3}")

# Example usage

insertionSort(arr3)
print("Sorted array:", arr3)

print("\n##########  Quick sort algo  ##########\n")
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
print(f"Before iteration : {my_array}")

def partition(array, low, high):
    # Choose the pivot element (last element in the range)
    pivot = array[high]
    # i represents the boundary of elements smaller than or equal to the pivot
    i = low - 1

    # Iterate through the elements in the range [low, high-1]
    for j in range(low, high):
        if array[j] <= pivot:  # If the current element is less than or equal to the pivot
            i += 1  # Move the boundary of smaller elements to the right
            # Swap the current element with the element at the boundary
            array[i], array[j] = array[j], array[i]

    # Place the pivot element in its correct position
    array[i+1], array[high] = array[high], array[i+1]
    print(f"Pivot placed at index {i+1}: {array}")  # Print the array after placing the pivot
    return i+1  # Return the index of the pivot

def quicksort(array, low=0, high=None):
    # If no high index is provided, set it to the last index of the array
    if high is None:
        high = len(array) - 1

    # Base condition: If the range has more than one element
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(array, low, high)
        # Recursively sort the elements before the pivot
        quicksort(array, low, pivot_index-1)
        # Recursively sort the elements after the pivot
        quicksort(array, pivot_index+1, high)
        # Print the array after sorting the current range
        print(f"After sorting between indices {low} and {high}: {array}")

# Example usage
my_array = [10, 7, 8, 9, 1, 5]
quicksort(my_array)
print("Sorted array:", my_array)

print("\n##########  Counting sort algo  ##########\n")

my_array1 = [4, 4, 2, 2, 2, 9, 7, 8, 8, 3, 3]
print(f"Before iteration : {my_array1}")

def countSort(arr):
    # find max value to determine range od count array
    max_val = max(arr)
    # create count array the size of max_val, initialised to 0
    count = [0] * (max_val + 1)

    # for nums in arr, add to each matched index in count array
    for num in arr:
        count[num] += 1
    print(count)

    # created sorted array
    sorted_array = []
    for i in range(len(count)):
        #adds each batch of numbers to array 1*0, 2*[2, 2, 2], 3*[3,3]
        sorted_array.extend([i] *( count[i] ))

    return sorted_array

print(f"Sorted array : {countSort(my_array1)}")


print("\n##########  Merge sort algo  ##########\n")
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]  # Input array
print(f"Before iteration : {unsortedArr}")

def mergeSort(arr):
    # Base case: if the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array to split it into two halves
    mid = len(arr) // 2
    leftHalf = arr[:mid]  # Left half of the array
    rightHalf = arr[mid:]  # Right half of the array

    # Recursively sort both halves
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # Merge the sorted halves and return the result
    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []  # To store the merged and sorted elements
    i = j = 0  # Pointers for both halves

    # Compare elements from both halves and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    result.extend(left[i:])
    # Add any remaining elements from the right half
    result.extend(right[j:])

    return result

# Example usage
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]  # Input array
sortedArr = mergeSort(unsortedArr)  # Perform merge sort
print("Sorted array:", sortedArr)  # Print the sorted array

print("\n##########  Linear search algo  ##########\n")


def linear_search(arr, target):
    # Iterate through each element in the array
    for index in range(len(arr)):
        # Check if the current element matches the target
        if arr[index] == target:
            print(f"Element {target} found at index {index}")
            return index  # Return the index where the target was found

    # If the loop completes without finding the target
    print(f"Element {target} not found in the array")
    return -1  # Return -1 to indicate the target is not in the array

# Example usage
unsortedArr = [4, 2, 9, 7, 8, 3]
target = 7
result = linear_search(unsortedArr, target)
print("Search result:", result)

print("\n##########  Binary search algo  ##########\n")
# array has to be sorted

def binarySearch(arr, target):
    # Initialize the search bounds
    left = 0
    right = len(arr) - 1

    # Continue searching while the bounds are valid
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1  # Narrow search to the right half
        else:
            right = mid - 1  # Narrow search to the left half

    # If the target is not found, return -1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15]  # Sorted input array
target = 7

# Perform binary search
result = binarySearch(arr, target)

# Check the result and print the appropriate message
if result != -1:
    print("Value", target, "found at index", result)
else:
    print("Value", target, "not found")