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