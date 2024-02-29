**Aula 1: Estruturas de Dados e Manipulação de Arquivos em Python**

Nesta fase, aprofundaremos nossos conhecimentos em Python, explorando estruturas de dados e a manipulação de arquivos. Dominar esses conceitos é crucial para qualquer desenvolvedor, pois oferece poderosas ferramentas para armazenamento e manipulação eficientes de informações.



**1. Estruturas de Dados em Python**

Python oferece uma rica variedade de estruturas de dados que permitem aos desenvolvedores manipular e organizar dados de maneira eficiente. Vamos explorar algumas das estruturas de dados mais fundamentais e avançadas em Python, juntamente com exemplos de código para ilustrar seu uso.

**1.1 Listas**

As listas são uma das estruturas de dados mais versáteis em Python, permitindo armazenar uma coleção ordenada de elementos.

```python
# Exemplo de lista
frutas = ['maçã', 'banana', 'laranja']
print(frutas)

# Acessar elementos
primeira_fruta = frutas[0]
print(primeira_fruta)

# Adicionar elemento
frutas.append('uva')
print(frutas)

# Remover elemento
frutas.remove('banana')
print(frutas)
```

**1.2 Tuplas**

Tuplas são semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação.

```python
# Exemplo de tupla
coordenadas = (3, 4)
print(coordenadas)

# Desempacotamento de tupla
x, y = coordenadas
print(f'x: {x}, y: {y}')
```

**1.3 Conjuntos**

Conjuntos são coleções não ordenadas de elementos únicos.

```python
# Exemplo de conjunto
cores = {'vermelho', 'verde', 'azul'}
print(cores)

# Adicionar elemento
cores.add('amarelo')
print(cores)

# Operações de conjunto
outras_cores = {'roxo', 'vermelho', 'verde'}
comum = cores.intersection(outras_cores)
print(comum)
```

**1.4 Dicionários**

Dicionários permitem associar valores a chaves, oferecendo uma estrutura de mapeamento.

```python
# Exemplo de dicionário
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'Exemplo'}
print(pessoa)

# Acessar valor por chave
print(pessoa['idade'])

# Adicionar nova chave-valor
pessoa['profissao'] = 'Desenvolvedor'
print(pessoa)
```


**2. Manipulação de Arquivos em Python**

Começaremos aprendendo a lidar com arquivos, uma tarefa essencial em muitos projetos. Python fornece funções simples e poderosas para abrir, ler e escrever em arquivos.

A manipulação de arquivos é uma parte crucial do desenvolvimento de software, e em Python, essa tarefa é simplificada por uma variedade de recursos e funções poderosas. Exploraremos os principais métodos e técnicas para lidar com arquivos em Python, desde a leitura e escrita básicas até operações mais avançadas.

**Leitura e Escrita Básicas**

**2.1 Leitura de Arquivos**

Para ler o conteúdo de um arquivo em Python, utilizamos a função `open()` junto com o método `read()`:

```python
# Exemplo de leitura de um arquivo
with open('arquivo.txt', 'r') as file:
    content = file.read()
    print(content)
```

A declaração `with` é utilizada para garantir que o arquivo seja fechado corretamente após a leitura.

**2.2 Escrita em Arquivos**

Para escrever em um arquivo, utilizamos o modo `'w'` (write) ao abrir o arquivo:

```python
# Exemplo de escrita em um arquivo
with open('novo_arquivo.txt', 'w') as file:
    file.write('Conteúdo a ser escrito no arquivo.')
```

**2.3 Leitura Linha a Linha**

Caso seja necessário ler um arquivo linha a linha, podemos utilizar um loop `for`:

```python
# Exemplo de leitura de um arquivo linha a linha
with open('arquivo.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() remove espaços em branco e caracteres de nova linha
```

**2.4 Anexar Conteúdo a um Arquivo**

Se desejarmos adicionar conteúdo a um arquivo sem substituir o existente, usamos o modo `'a'` (append):

```python
# Exemplo de anexar conteúdo a um arquivo
with open('arquivo.txt', 'a') as file:
    file.write('\nNova linha de conteúdo adicionada.')
```

**2.5 Manipulação de Diretórios**

O módulo `os` em Python oferece funcionalidades para manipulação de diretórios. Por exemplo, para verificar se um diretório existe:

```python
import os

if os.path.exists('diretorio'):
    print('O diretório existe.')
else:
    print('O diretório não existe.')
```

**2.6 Trabalhando com JSON**

Para trabalhar com arquivos JSON, podemos usar o módulo `json`:

```python
import json

# Leitura de um arquivo JSON
with open('dados.json', 'r') as file:
    data = json.load(file)
    print(data)

# Escrita em um arquivo JSON
dados = {'nome': 'John', 'idade': 30, 'cidade': 'Exemplo'}
with open('dados.json', 'w') as file:
    json.dump(dados, file)
```



**Exercícios Práticos:**

1. Crie um arquivo de texto contendo uma lista de itens.
2. Leia o arquivo criado, exibindo seu conteúdo.
3. Utilize uma lista para armazenar os números de 1 a 10 e remova os números pares.
4. Crie um dicionário com informações de contatos (nome, e-mail, telefone) e permita a busca por um contato específico.

Estes exercícios práticos irão solidificar seu entendimento sobre manipulação de arquivos e estruturas de dados em Python. Ao aplicar esses conceitos, você estará preparado para lidar eficientemente com informações e estruturar dados em seus futuros projetos. A jornada continua, e essas habilidades serão fundamentais em cada passo do seu caminho como desenvolvedor Python.

## Resolução dos exercícios

Vamos resolver os exercícios passo a passo:

### Exercício 1: Criar um arquivo de texto contendo uma lista de itens.

```python
# Conteúdo da lista
itens = ["item1", "item2", "item3", "item4", "item5"]

# Escrever a lista no arquivo
with open('lista_itens.txt', 'w') as file:
    for item in itens:
        file.write(item + '\n')
```

### Exercício 2: Ler o arquivo criado, exibindo seu conteúdo.

```python
# Ler o conteúdo do arquivo
with open('lista_itens.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)
```

### Exercício 3: Utilizar uma lista para armazenar os números de 1 a 10 e remover os números pares.

```python
# Criar uma lista de números de 1 a 10
numeros = list(range(1, 11))

# Remover números pares da lista
numeros = [num for num in numeros if num % 2 != 0]

# Exibir a lista resultante
print(numeros)
```

### Exercício 4: Criar um dicionário com informações de contatos e permitir a busca por um contato específico.

```python
# Criar um dicionário de contatos
contatos = {
    'Joao': {'email': 'joao@example.com', 'telefone': '123456789'},
    'Maria': {'email': 'maria@example.com', 'telefone': '987654321'},
    'Carlos': {'email': 'carlos@example.com', 'telefone': '555555555'}
}

# Função para buscar um contato específico
def buscar_contato(nome):
    if nome in contatos:
        return contatos[nome]
    else:
        return 'Contato não encontrado.'

# Exemplos de busca
print(buscar_contato('Joao'))
print(buscar_contato('Ana'))
```

Esses códigos abordam cada um dos exercícios propostos. Certifique-se de adaptar os nomes dos arquivos e os dados conforme necessário para o seu contexto.