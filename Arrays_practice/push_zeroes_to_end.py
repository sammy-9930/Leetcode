"""
Time complexity: O(n)
Space complexity: O(n)
"""
def push_zeros_to_end(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] != 0:
            res.append(arr[i])
            i += 1
    while len(res) < len(arr):
        res.append(0)
    return res 

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print("initial array: ",arr)
print("final result: ", push_zeros_to_end(arr))


"""
Time complexity: O(n)
Space complexity: O(1)
"""
def push_zeros_to_end(arr):
    count = 0
    for number in arr:
        if number != 0:
            arr[count] = number
            count += 1 
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print("initial array: ",arr)
print("final result: ", push_zeros_to_end(arr))


# ip_nums = [1, 0, 2, 0, 3, 0, 4, 0]
# op_nums = [1, 2, 3, 4, 0, 0, 0, 0]

def sort(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1 
    return arr 
            
arr =  [1, 0, 2, 0, 3, 0, 4, 0]
print(sort(arr))

