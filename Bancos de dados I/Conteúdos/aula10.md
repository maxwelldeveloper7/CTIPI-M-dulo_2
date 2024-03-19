**Aula 21-22: Dependência Funcional e Chaves em Banco de Dados**

*Navegando pela Estrutura da Informação*

Nesta aula, exploraremos conceitos fundamentais de dependência funcional e chaves em Banco de Dados. Compreenderemos como esses elementos são essenciais para garantir a integridade dos dados e a eficiência das operações de consulta e atualização.

**1. Dependência Funcional: A Essência da Relação**

A dependência funcional descreve a relação entre dois conjuntos de atributos em uma tabela de Banco de Dados. Se o valor de um conjunto de atributos determina unicamente o valor de outro conjunto, dizemos que há uma dependência funcional entre eles.

*Ilustração: Exemplo de Dependência Funcional*

![Dependência Funcional](link_para_imagem1)

Por exemplo, em uma tabela de funcionários, o número de identificação do funcionário determina unicamente o nome do funcionário. Portanto, há uma dependência funcional entre o número de identificação e o nome.

**2. Chaves em Banco de Dados: Identificando Unicidade**

As chaves são atributos ou conjuntos de atributos que permitem identificar de forma única cada tupla em uma tabela de Banco de Dados. Existem diferentes tipos de chaves, como chaves primárias, chaves candidatas e chaves estrangeiras.

*Ilustração: Tipos de Chaves em Banco de Dados*

![Tipos de Chaves](link_para_imagem2)

- Chave Primária: É a chave principal que identifica exclusivamente cada registro em uma tabela. Não pode conter valores nulos e deve ser única para cada tupla.
- Chave Candidata: São atributos que podem ser chaves primárias, mas ainda não foram escolhidos como tal. Também devem ser únicos e não nulos.
- Chave Estrangeira: É um conjunto de atributos em uma tabela que faz referência à chave primária de outra tabela. Isso estabelece uma relação entre as tabelas.

**3. Garantindo a Integridade dos Dados**

A compreensão das dependências funcionais e das chaves em Banco de Dados é crucial para garantir a integridade dos dados. Ao identificar e definir corretamente as chaves, podemos evitar inconsistências e redundâncias nos registros.

*Ilustração: Garantindo a Integridade dos Dados*

![Integridade dos Dados](link_para_imagem3)

Por exemplo, ao definir uma chave primária em uma tabela de clientes, garantimos que cada cliente seja exclusivamente identificado por um número único de cliente. Isso evita a duplicação de informações e facilita a manutenção dos dados.

**4. Normalização de Banco de Dados: O Papel das Dependências Funcionais**

A normalização é um processo de organização de dados em um Banco de Dados para reduzir redundâncias e melhorar a integridade dos dados. As dependências funcionais desempenham um papel crucial nesse processo, ajudando a identificar e resolver problemas de redundância.

*Ilustração: Normalização de Banco de Dados*

![Normalização](link_para_imagem4)

Ao aplicar a normalização, dividimos as tabelas em estruturas mais simples e bem definidas, garantindo que cada tabela represente apenas uma entidade ou relação. Isso reduz a redundância e facilita a manutenção dos dados.

**Conclusão: A Base para um Banco de Dados Eficiente**

Dependências funcionais e chaves são os alicerces de um Banco de Dados eficiente e bem estruturado. Ao compreendermos esses conceitos fundamentais, estamos preparados para projetar e gerenciar sistemas de informação robustos e confiáveis. Nos próximos encontros, exploraremos técnicas avançadas de modelagem e manipulação de dados para expandir ainda mais nosso domínio sobre o mundo dos Banco de Dados.

**Atividade Avaliativa - Aula 21-22: Dependência Funcional e Chaves em Banco de Dados**

*Instruções: Escolha a alternativa correta para cada pergunta.*

1. **O que descreve a dependência funcional em um Banco de Dados?**
   a) A relação entre dois conjuntos de atributos onde um determina unicamente o valor do outro.
   b) A relação entre duas tabelas em um DER.
   c) A quantidade de instâncias de uma entidade em um relacionamento.
   d) A representação gráfica de uma relação no DER.

2. **Qual é o principal objetivo de uma chave primária em uma tabela de Banco de Dados?**
   a) Identificar de forma única cada registro em uma tabela.
   b) Permitir valores nulos em uma tabela.
   c) Estabelecer uma relação entre diferentes tabelas.
   d) Representar graficamente as dependências entre os atributos.

3. **O que são chaves candidatas em um Banco de Dados?**
   a) Atributos que podem ser chaves primárias, mas ainda não foram escolhidos como tal.
   b) Atributos que podem ser nulos em uma tabela.
   c) Conjuntos de atributos que determinam o valor de outro conjunto.
   d) Conjuntos de atributos que são exclusivos em uma tabela.

4. **Qual é o papel das chaves estrangeiras em um Banco de Dados?**
   a) Referenciar a chave primária de outra tabela, estabelecendo uma relação entre elas.
   b) Identificar de forma única cada registro em uma tabela.
   c) Descrever a relação entre dois conjuntos de atributos.
   d) Permitir valores repetidos em uma tabela.

5. **Por que a compreensão das dependências funcionais e das chaves é fundamental em Banco de Dados?**
   a) Para garantir a integridade dos dados e evitar redundâncias.
   b) Para representar graficamente as tabelas em um DER.
   c) Para permitir valores nulos em uma tabela.
   d) Para estabelecer relações entre diferentes tabelas.

**Gabarito:**
1. a) A relação entre dois conjuntos de atributos onde um determina unicamente o valor do outro.
2. a) Identificar de forma única cada registro em uma tabela.
3. a) Atributos que podem ser chaves primárias, mas ainda não foram escolhidos como tal.
4. a) Referenciar a chave primária de outra tabela, estabelecendo uma relação entre elas.
5. a) Para garantir a integridade dos dados e evitar redundâncias.