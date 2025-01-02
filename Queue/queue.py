from collections import deque 

"""Enqueue : add element to end of the queue"""
queue = []
queue.append(10)
queue.append(20)
print(queue)


"""Dequeue: removes element at the front of the queue"""
queue_1 = [10, 20, 30]
front_element_1 = queue_1.pop(0)
print("Front element: ",front_element_1)
print(queue_1)


"""Using deque class from python collections module"""
queue_2 = deque()
queue_2.append(10)
queue_2.append(20)
print("initial queue: ", queue_2)
front_element_2 = queue_2.popleft()
print("front element: ",front_element_2)
