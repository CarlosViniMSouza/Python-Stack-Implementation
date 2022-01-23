myStack = []

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)
# Output: ['a', 'b', 'c']

print(myStack.pop())
# Output: 'c'

print(myStack.pop())
# Output: 'b'

print(myStack.pop())
# Output: 'a'

print(myStack.pop())
"""
Output:

Traceback (most recent call last):
  File "E:\Programacao\PythonDjango\Python-Stack\code\code_num1.py", line 19, in <module>
    print(myStack.pop())
IndexError: pop from empty list

Process finished with exit code 1
"""