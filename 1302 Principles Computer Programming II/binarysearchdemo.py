# You need a .txt file with words in it to have this program work
file = open(input('file name: '), 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))


def binary_search(arr, target):

    iteration = 0
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        iteration = iteration + 1

        if target == arr[mid]:
            break

        elif target < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    if mid == 0:
        mid = -1

    print('Target = ' + target + ', Found at Index = ' + str(mid + 1) + ', Number of iterations = ' + str(iteration))


target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()


