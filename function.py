def printZigZagConcat(str, n):

    # Corner Case (Only one row)
    if n == 1:
        print(str)
        return

    # Find length of string
    l = len(str)

    # Create an array of
    # strings for all n rows
    arr = ["" for x in range(l)]

    # Initialize index for
    # array of strings arr[]
    row = 0

    # Traverse through
    # given string
    for i in range(l):

        # append current character
        # to current row
        arr[row] += str[i]

        # If last row is reached,
        # change direction to 'up'
        if row == n - 1:
            down = False

        # If 1st row is reached,
        # change direction to 'down'
        elif row == 0:
            down = True

        # If direction is down,
        # increment, else decrement
        if down:
            row += 1
        else:
            row -= 1

    # Print concatenation
    # of all rows
    for i in range(n):
        print(arr[i], end="")


def zigzag(arr):
    n = len(arr)
    # Flag true indicates relation "<" is expected,
    # else ">" is expected. The first expected relation
    # is "<"
    flag = True
    for i in range(n-1):
        # "<" relation expected
        if flag is True:
            # If we have a situation like A > B > C,
            # we get A > C < B
            # by swapping B and C
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            # ">" relation expected
        else:
            # If we have a situation like A < B < C,
            # we get A < C > B
            # by swapping B and C
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1 - flag)
    return (arr)


def zigzag_sort(arr):
    n = len(arr)
    # use sort function to sort the array
    arr.sort()
    # traverse the array from 1 to n-1
    for i in range(1, n-1, 2):
      # swap value of current element with next element
        arr[i], arr[i+1] = arr[i+1], arr[i]
    # print the array
    return (arr)
