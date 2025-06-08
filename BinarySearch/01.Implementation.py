def binary_search(num, array):
    low = 0
    high = len(array) - 1

    while (low <= high):
        middle_index = (low + high ) // 2
        middle_number = array[middle_index]
        if middle_number == num:
            return True
        else:
            if middle_number > num:
                high = middle_index-1
            else:
                low = middle_index+1
    return False


arr1 = [1,2,3,4,5]
arr2 = [2,4,6,8,10]

print(binary_search(5, arr1)) # Returns True
print(binary_search(1, arr2)) # Returns False