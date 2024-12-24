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


