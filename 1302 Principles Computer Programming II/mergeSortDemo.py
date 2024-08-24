def merge_sort(arr, left, right):
    if left < right:

        # this part of the program right under this comment splits the list in half and starts 2 merge sorts
        # one with the left and one with the right side of the list and then continues to split them on each
        # side of the splits run through the merge sort

        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)

        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    merged_size = right - left + 1
    merged = [0]*merged_size
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        # this part works down the list and compares it to the other numbers in the list to see where it belongs
        if arr[i] < arr[j]:
            merged[k] = arr[i]
            i += 1

        else:
            merged[k] = arr[j]
            j += 1

        k += 1

    # continues to use the splits to sort out and compare list proporties and then sorts it accordingly
    while i <= mid:
        merged[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        merged[k] = arr[j]
        j += 1
        k += 1

    k = 0

    while k < merged_size:
        arr[left + k] = merged[k]
        k += 1


# takes the variable list of numbers and the left right propories defiend in the merge
# sort funtion and uses the output to print out the sorted list

nums = []
on = True

while on:
    num = input('Num value (type quit to stop): ')

    if num == 'quit':
        on = False
        print('\n')

    else:
        nums.append(int(num))
        print(nums)

merge_sort(nums, 0, len(nums) - 1)
for num in nums:
    print(num, end=' ')
