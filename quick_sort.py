def quick_sort(array: list):
    array_length = len(array)

    if array_length <= 1:
        return array

    pivot = array[array_length // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = [64, 35, 25, 12, 11, 29, 84, 92]

print(f"Sorted array is: {quick_sort(arr)}")
