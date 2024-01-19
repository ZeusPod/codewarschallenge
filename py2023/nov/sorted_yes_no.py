def is_sorted_and_how(arr):
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return 'Ordenada en ascendente'
    elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return 'Ordenada en descendente'
    else:
        return 'No está ordenada'

print(is_sorted_and_how([3,4,9,6,7]))
