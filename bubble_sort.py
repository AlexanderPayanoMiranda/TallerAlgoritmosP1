def bubble_sort(array: list):
    array_length = len(array)

    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


arr = [64, 35, 25, 12, 11, 29, 84, 92]

print(f"Sorted array is: {bubble_sort(arr)}")
