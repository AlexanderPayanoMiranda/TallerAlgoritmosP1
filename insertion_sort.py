def insertion_sort(array: list):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


arr = [64, 35, 25, 12, 11, 29, 84, 92]

print(f"Sorted array is: {insertion_sort(arr)}")
