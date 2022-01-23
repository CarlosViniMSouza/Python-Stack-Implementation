"""
-> Usando collections.deque para criar uma pilha Python

O módulo de coleções contém deque, que é útil para criar pilhas Python.
'deque' é pronunciado “deck” e significa “fila de extremidade dupla”.

Você pode usar os mesmos métodos no deque que viu acima para list,
.append() e .pop():
"""

from collections import deque

myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')

print(myStack)
# Output: deque(['a', 'b', 'c'])

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
