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


def zigzag_matrix(matrix, n_col, is_transpose):

    rows = len(matrix)
    columns = n_col

    if(is_transpose):
        matrix = matrix.transpose()
        columns = rows
        rows = n_col

    solution = [[] for i in range(rows+columns-1)]

    for i in range(rows):
        for j in range(columns):
            sum = i+j
            if(sum % 2 == 0):

                # add at beginning
                solution[sum].insert(0, matrix[i][j])
            else:

                # add at end of the list
                solution[sum].append(matrix[i][j])

    result = ''
    # print the solution as it as
    for i in solution:
        for j in i:
            result += (j+"")
    return result


def create_matrix(arr, n_col):
    matrix = []
    temp_row = []
    for x in range(len(arr)):
        no = x+1
        temp_row.append(arr[x])
        if(no % n_col == 0):
            matrix.append(temp_row)
            temp_row = []
    return matrix


# -------------------------------------------------- incomplete now --------------------
def findOrder(matrix):
    n = 0  # ?????????????????
    m = 0  # ?????????????????
    result = [0]*(n*m)
    result[0] = matrix[0][0]
    k = 1
    i = j = 0
    while(k < n*m):
        while i >= 1 and j < n-1:
            i -= 1
            j += 1
            result[k] = matrix[i][j]
            k += 1
        if j < n-1:
            j += 1
            result[k] = matrix[i][j]
            k += 1
        elif i < m-1:
            i += 1
            result[k] = matrix[i][j]
            k += 1
        while i < m-1 and j >= 1:
            i += 1
            j -= 1
            result[k] = matrix[i][j]
            k += 1
        if i < m-1:
            i += 1
            result[k] = matrix[i][j]
            k += 1
        elif j < n-1:
            j += 1
            result[k] = matrix[i][j]
            k += 1
    return result
