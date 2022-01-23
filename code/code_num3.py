"""
Embora a interface para lista e deque fosse semelhante, o LifoQueue
usa .put() e .get() para adicionar e remover dados da pilha
"""

from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')
myStack.put('b')
myStack.put('c')

print(myStack)
# Output: <queue.LifoQueue object at 0x7f408885e2b0>

print(myStack.get())
# Output: 'c'
print(myStack.get())
# Output: 'b'
print(myStack.get())
# Output: 'a'

# myStack.get() <--- waits forever
print(myStack.get_nowait())
"""
Output:

Traceback (most recent call last):
  File "E:\Programacao\PythonDjango\Python-Stack\code\code_num3.py", line 24, in <module>
    print(myStack.get_nowait())
  File "C:\Users\CarlosViniMSouza\AppData\Local\Programs\Python\Python310\lib\queue.py", line 199, in get_nowait
    return self.get(block=False)
  File "C:\Users\CarlosViniMSouza\AppData\Local\Programs\Python\Python310\lib\queue.py", line 168, in get
    raise Empty
_queue.Empty
"""

"""
Ao contrário do deque, o LifoQueue foi projetado para ser totalmente seguro
para threads. Todos os seus métodos são seguros para uso em um ambiente encadeado. 
Ele também adiciona tempos limite opcionais às suas operações que podem frequentemente 
ser um recurso obrigatório em programas encadeados.
"""
