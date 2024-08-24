def quick_sort(arr, start, end):
    if start >= end:
        return

    k = partition(arr, start, end)
    quick_sort(arr, start, k - 1)
    quick_sort(arr, k + 1, end)


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    print('------ Quick sorting from index:  ' + str(low) + '  to  ' + str(high) + '  -----')
    print('Array segment before partitioning:  ' + str(arr[low:high+1]) + ' , Pivot:  ' + str(pivot))

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    print('Array segment after partitioning:  ' + str(arr[low:high+1]) + '\n')

    return i


# arr = [11, 12, 1, 9, 6, 5, 4, 7]

arr = []
on = True

while on:
    num = input('Num value (type quit to stop): ')

    if num == 'quit':
        on = False
        print('\n')

    else:
        arr.append(int(num))
        print(arr)

# Takes an inpute of numbers and sorts it from least to greatest using the quick sort alg

quick_sort(arr, 0, len(arr)-1)
print('The final sorted array', arr)
