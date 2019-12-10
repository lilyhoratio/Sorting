# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loop through i to end of list
        for j in range(cur_index + 1, len(arr)):
            # if number after is smaller than current smallest number, reassign index of smallest
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if smallest_index != cur_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index],
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = False
        if swapped:
            break
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr