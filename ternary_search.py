def ternary_search(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if array[mid1] == x:
            return mid1
        elif array[mid2] == x:
            return mid2
        elif x < array[mid1]:
            right = mid - 1
        elif x > array[mid2]:
            left = mid2 + 1
        else:
            left = mid + 1
            right = mid2 - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 4

result = ternary_search(arr, x)

if result != -1:
    print(f"El elemento se encontro en el index:{str(result)}")
else:
    print("El elemento no se encontro")
