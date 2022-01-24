## O que é uma pilha?

### Uma [pilha](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) é uma [estrutura de dados](https://realpython.com/python-data-structures/) que armazena itens da maneira Last-In/First-Out. Isto é frequentemente referido como LIFO. Isso contrasta com uma [fila](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)), que armazena itens de maneira FIFO (First-In/First-Out).

### Provavelmente é mais fácil entender uma pilha se você pensar em um caso de uso com o qual provavelmente está familiarizado: o recurso _Desfazer_ em seu editor.

### Vamos imaginar que você está editando um arquivo Python para que possamos ver algumas das operações que você realiza. Primeiro, você adiciona uma nova função. Isso adiciona um novo item à pilha de desfazer:

![img1_stack](https://files.realpython.com/media/stack_push_add_function.b406cffbe2dd.png)

### Você pode ver que a pilha agora tem uma operação _Add Function_ nela. Depois de adicionar a função, você exclui uma palavra de um comentário. Isso também é adicionado à pilha de desfazer:

![img2_stack](https://files.realpython.com/media/stack_push_delete_word.6a64fed15fde.png)

### Observe como o item Excluir Word é colocado no topo da pilha. Por fim, você recua um comentário para que fique alinhado corretamente:

![img3_stack](https://files.realpython.com/media/stack_push_indent.01223b7d94a7.png)

### Você pode ver que cada um desses comandos é armazenado em uma pilha de desfazer, com cada novo comando sendo colocado no topo. Quando você está trabalhando com pilhas, adicionar novos itens como esse é chamado de `push`.

### Agora você decidiu desfazer todas as três alterações, então você pressiona o comando desfazer. Ele pega o item no topo da pilha, que estava recuando o comentário, e remove isso da pilha:

![img4_stack](https://files.realpython.com/media/stack_pop_indent.e28029c81831.png)

### Seu editor desfaz o recuo e a pilha de desfazer agora contém dois itens. Esta operação é o oposto de `push` e é comumente chamada de `pop`.

### Quando você pressiona desfazer novamente, o próximo item é retirado da pilha:

![img5_stack](https://files.realpython.com/media/stack_pop_delete_word.89f14f6ed390.png)

### Isso remove o item Excluir palavra, deixando apenas uma operação na pilha.

### Finalmente, se você clicar em Desfazer uma terceira vez, o último item será retirado da pilha:

![img6_stack](https://files.realpython.com/media/stack_pop_add_function.a4f66332971a.png)

### A pilha de desfazer agora está vazia. Clicar em _Desfazer_ novamente depois disso não terá efeito porque sua pilha de desfazer está vazia, pelo menos na maioria dos editores. Você verá o que acontece quando chama `.pop()` em uma pilha vazia nas descrições de implementação abaixo.

## Implementando uma pilha Python

### Existem algumas opções quando você está implementando uma pilha Python. Este artigo não cobrirá todos eles, apenas os básicos que atenderão a quase todas as suas necessidades. Você se concentrará em usar estruturas de dados que fazem parte da biblioteca Python, em vez de escrever suas próprias ou usar pacotes de terceiros.
### Você verá as seguintes implementações de pilha do Python:

```
° Lista
° coleções.deque
° fila.LifoQueue
```

## Usando a `lista` para criar uma pilha Python

### A estrutura de `lista` interna que você provavelmente usa com frequência em seus programas pode ser usada como uma pilha. Em vez de `.push()`, você pode usar [`.append()`](https://realpython.com/python-append/) para adicionar novos elementos ao topo de sua pilha, enquanto `.pop()` remove os elementos na ordem LIFO:

```python
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
```
