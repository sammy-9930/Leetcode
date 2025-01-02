"""Push to stack"""
stack = []
stack.append(10)
stack.append(20)
print(stack) # o/p: [10, 20]

"""Pop from stack"""
stack_1 = [10, 20, 30]
top_element = stack.pop()
print(top_element)
print(stack_1)

"""Peek a stack"""
stack_2 = [10, 20, 30]
top_element_1 = stack_2[-1]
print(top_element)