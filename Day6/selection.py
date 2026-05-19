#Selection Sort

arr=[20,15,12,10,2]
print(arr)
for i in range(len(arr)):
    min_index = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[min_index]:
            min_index = j
        j += 1
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
    print("------------")
print("Sorted Array: ", arr)    


#output:
# [20, 15, 12, 10, 2]
# [2, 15, 12, 10, 20]
# ------------
# [2, 10, 12, 15, 20]
# ------------
# [2, 10, 12, 15, 20]
# ------------
# [2, 10, 12, 15, 20]
# ------------
# [2, 10, 12, 15, 20]
# ------------
# Sorted Array:  [2, 10, 12, 15, 20]