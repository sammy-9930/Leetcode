"""Brute force solution"""
def stock(arr):
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    return max_profit
            

arr = [7,1,5,3,6,4]
print(stock(arr))

"""Optimized solution"""
def stock(arr):
    max_profit = 0
    buy_price = arr[0]
    for price in arr:
        if price < buy_price:
            buy_price = price 
        profit = price - buy_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

arr = [7,1,5,3,6,4]
print(stock(arr))