import math


def jump_search(arr, x):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0

    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[int(prev)] == x:
        return prev

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 4

result = jump_search(arr, x)

if result != -1:
    print(f"El elemento se encontro en el index:{str(result)}")
else:
    print("El elemento no se encontro")
