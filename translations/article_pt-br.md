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

### Você pode ver no comando final que uma `lista` irá gerar um `IndexError` se você chamar `.pop()` em uma pilha vazia.

### `lista` tem a vantagem de ser familiar. Você sabe como funciona e provavelmente já o usou em seus programas.

### Infelizmente, a `lista` tem algumas deficiências em comparação com outras estruturas de dados que você verá. O maior problema é que ele pode ter problemas de velocidade à medida que cresce. Os itens em uma `lista` são armazenados com o objetivo de fornecer acesso rápido a elementos aleatórios na `lista`. Em um nível alto, isso significa que os itens são armazenados um ao lado do outro na memória.

### Se sua pilha ficar maior do que o bloco de memória que a contém atualmente, o Python precisa fazer algumas alocações de memória. Isso pode fazer com que algumas chamadas `.append()` demorem muito mais do que outras.

### Há um problema menos grave também. Se você usar `.insert()` para adicionar um elemento à sua pilha em uma posição diferente do final, pode demorar muito mais. Isso normalmente não é algo que você faria com uma pilha, no entanto.

### A próxima estrutura de dados o ajudará a contornar o problema de realocação que você viu com a `lista`.

## Usando `collections.deque` para criar uma pilha Python

### O módulo de `coleções` contém [`deque`](https://docs.python.org/3/library/collections.html#collections.deque), que é útil para criar pilhas Python. `deque` é pronunciado “deck” e significa “fila de extremidade dupla”.

### Você pode usar os mesmos métodos no `deque` que viu acima para list, `.append()` e `.pop()`:

```python
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
```

### Isso parece quase idêntico ao exemplo de `lista` acima. Neste ponto, você pode estar se perguntando por que os desenvolvedores principais do Python criariam duas estruturas de dados com a mesma aparência.

## Pilhas e Threading do Python

### As pilhas do Python também podem ser úteis em programas multithread, mas se você não estiver interessado em threading, pode pular esta seção com segurança e pular para o resumo.

### As duas opções que você viu até agora, `lista` e `deque`, se comportam de forma diferente se o seu programa tiver threads.

### Para começar pelo mais simples, você nunca deve usar `lista` para qualquer estrutura de dados que possa ser acessada por vários threads. `lista` não é thread-safe.

**Observação**: se você precisar de uma atualização sobre segurança de encadeamento e condições de corrida, confira [Uma Introdução a Threading em Python](https://realpython.com/intro-to-python-threading/).

### Embora a interface para lista e deque fosse semelhante, o LifoQueue usa .put() e .get() para adicionar e remover dados da pilha

```python
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
```

### Ao contrário do `deque`, o `LifoQueue` foi projetado para ser totalmente seguro para threads. Todos os seus métodos são seguros para uso em um ambiente encadeado. Ele também adiciona tempos limite opcionais às suas operações que podem frequentemente ser um recurso obrigatório em programas encadeados.

### No entanto, essa segurança de thread completa tem um custo. Para alcançar esta segurança de rosca, O `LifoQueue` precisa fazer um pouco de trabalho extra em cada operação, o que significa que levará um pouco mais de tempo.

### Frequentemente, essa pequena lentidão não importa para a velocidade geral do programa, mas se você mediu seu desempenho e descobriu que suas operações de pilha são o gargalo, pode valer a pena alternar cuidadosamente para um `deque`.

### Eu gostaria de enfatizar novamente que mudar de `LifoQueue` para `deque` porque é mais rápido sem ter medidas mostrando que suas operações de pilha são um gargalo é um exemplo de [otimização prematura](https://en.wikipedia.org/wiki/Program_optimization#When_to_optimize). Não faça isso.

## Pilhas Python: Qual implementação você deve usar?

### Em geral, você deve usar um `deque` se não estiver usando threading. Se você estiver usando threading, deve usar um `LifoQueue`, a menos que tenha medido seu desempenho e descoberto que um pequeno aumento na velocidade para empurrar e estourar fará diferença suficiente para garantir os riscos de manutenção.

### `lista` pode ser familiar, mas deve ser evitada porque pode ter problemas de realocação de memória. As interfaces para `deque` e `lista` são idênticas, e `deque` não tem esses problemas, o que torna `deque` a melhor escolha para sua pilha Python não encadeada.
