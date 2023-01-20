def binary_searchA(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def binary_searchB(array, x, low, high):
    if low <= high:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            return binary_searchB(array, x, mid+1, high)

        else:
            return binary_searchB(array, x, low, mid-1)
    else:
        return -1


arr = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = 13

resultA = binary_searchA(arr, x, 0, len(arr)-1)
resultB = binary_searchB(arr, x, 0, len(arr)-1)

if resultA != -1:
    print(f"El elemento se encontro en el index:{str(resultA)}")
else:
    print("El elemento no se encontro")

if resultB != -1:
    print(f"El elemento se encontro en el index:{str(resultB)}")
else:
    print("El elemento no se encontro")
