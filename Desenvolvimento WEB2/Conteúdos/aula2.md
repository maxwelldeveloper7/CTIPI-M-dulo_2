**Aula 2: Orientação a Objetos em Python**

Na primeira etapa de nossa jornada, vamos mergulhar no fascinante mundo da Orientação a Objetos (OOP) em Python. A OOP é um paradigma de programação que organiza o código em objetos, entidades que contêm dados e comportamentos. Em Python, a implementação da OOP é elegante e poderosa, proporcionando uma estrutura flexível para o desenvolvimento de software.

**1. Introdução à Orientação a Objetos**

Começamos com os conceitos fundamentais. Em Python, tudo é um objeto. Seja um número, uma string ou mesmo uma função, todos são objetos. A OOP formaliza essa ideia, permitindo-nos criar nossos próprios objetos com características únicas.

```python
# Exemplo básico de uma classe em Python
class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")

# Criando uma instância da classe Carro
meu_carro = Carro("Sedan", "Preto")
meu_carro.acelerar()
```

**2. Conceitos Chave da OOP**

Vamos explorar os pilares da OOP: encapsulamento, herança e polimorfismo. O encapsulamento protege os detalhes internos de uma classe, herança permite que uma classe herde características de outra, e polimorfismo possibilita que objetos de diferentes classes sejam tratados de maneira uniforme.

```python
# Exemplo de encapsulamento
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def obter_saldo(self):
        return self.__saldo

# Exemplo de herança
class ContaCorrente(ContaBancaria):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.limite = limite

# Exemplo de polimorfismo
conta1 = ContaBancaria(1000)
conta2 = ContaCorrente(1500, 500)

contas = [conta1, conta2]

for conta in contas:
    print(f"Saldo: {conta.obter_saldo()}")
```

**Exercícios Práticos:**

1. Crie uma classe `Pessoa` com atributos como nome, idade e método para exibir informações.
2. Implemente uma hierarquia de classes para modelar diferentes formas geométricas.
3. Crie uma classe `Animal` com métodos para emitir som e outra classe `Pato` que herde de `Animal` e tenha um método exclusivo `voar`.

Esses exercícios visam consolidar os conceitos de OOP em Python, proporcionando a oportunidade de aplicar os conhecimentos recém-adquiridos. Experimente criar instâncias, chamar métodos e explorar a flexibilidade que a Orientação a Objetos oferece. Estamos apenas começando nessa jornada, e o fascinante mundo da OOP aguarda por sua exploração!