**Aula 27-28: Exercícios Práticos de Projeto e Normalização**

*Aplicando Teoria à Prática*

Nesta aula, vamos aplicar os conceitos que aprendemos sobre projeto de Banco de Dados e normalização. Para garantir uma compreensão sólida, realizaremos exercícios práticos que envolverão a criação e a normalização de tabelas, identificando dependências e eliminando redundâncias.

**1. Entendendo a Estrutura do Banco de Dados**

O primeiro passo para o projeto de um Banco de Dados eficaz é compreender a estrutura necessária para uma determinada aplicação. Vamos iniciar com um exercício simples para criar um modelo conceitual básico que atenda às seguintes necessidades:

*Ilustração: Exemplo de Estrutura de Banco de Dados*

![Estrutura de Banco de Dados](link_para_imagem1)

- Uma empresa de vendas online deseja criar um Banco de Dados para gerenciar clientes, produtos, pedidos e entregas.
- O Banco de Dados deve permitir o registro de clientes com informações de contato, produtos com detalhes como nome, preço e descrição, e pedidos com associações entre clientes e produtos.

**2. Criando um Modelo Entidade-Relacionamento (MER)**

Com base nas necessidades identificadas, vamos criar um modelo entidade-relacionamento que define as relações entre as diferentes entidades. Este exercício envolve a definição de entidades, atributos, chaves primárias e chaves estrangeiras.

- **Clientes**: A entidade "Clientes" deve ter atributos como ID do cliente, nome, endereço e telefone. O ID do cliente será a chave primária.
- **Produtos**: A entidade "Produtos" deve incluir atributos como ID do produto, nome, descrição e preço. O ID do produto será a chave primária.
- **Pedidos**: A entidade "Pedidos" deve ter atributos como ID do pedido, data do pedido e ID do cliente (chave estrangeira para "Clientes").
- **Itens do Pedido**: Esta entidade é necessária para associar "Pedidos" e "Produtos", incluindo atributos como ID do pedido, ID do produto e quantidade.

*Ilustração: Modelo Entidade-Relacionamento*

![Modelo Entidade-Relacionamento](link_para_imagem2)

**3. Aplicando a Normalização**

Uma vez criado o modelo entidade-relacionamento, vamos aplicar a normalização para garantir a integridade e a eficiência do Banco de Dados. O objetivo é eliminar redundâncias, dependências parciais e transitivas, seguindo as formas normais.

- **Primeira Forma Normal (1FN)**: Cada coluna deve conter apenas valores atômicos. Se houver colunas com valores compostos ou grupos de valores, elas devem ser divididas em tabelas separadas.
- **Segunda Forma Normal (2FN)**: Se uma tabela tiver uma chave composta, todos os atributos não-chave devem depender de toda a chave primária, não apenas de parte dela.
- **Terceira Forma Normal (3FN)**: Para evitar dependências transitivas, cada atributo não-chave deve depender apenas da chave primária.

*Ilustração: Exemplo de Normalização*

![Normalização](link_para_imagem3)

**4. Exercícios Práticos de Normalização**

Agora, vamos realizar exercícios práticos para normalizar um modelo de Banco de Dados, identificando e eliminando dependências parciais e transitivas.

- Dada uma tabela que contém informações sobre alunos, disciplinas e notas, identificar se ela está em 1FN, 2FN ou 3FN.
- Se houver dependências transitivas, como elas podem ser eliminadas?
- Criar tabelas separadas para normalizar o modelo de dados, garantindo que cada atributo esteja na forma normal correta.

**Conclusão: Aplicando a Normalização na Prática**

Os exercícios práticos ajudam a consolidar o entendimento dos conceitos de projeto e normalização de Bancos de Dados. Através dessas atividades, conseguimos transformar teoria em prática, garantindo que os Bancos de Dados sejam eficientes, escaláveis e livres de redundâncias e anomalias. Nos próximos encontros, exploraremos técnicas avançadas de otimização e segurança em Banco de Dados para aprimorar ainda mais nossas habilidades.

Para implementar a resolução do exercício 4, precisamos resolver as seguintes questões relacionadas à normalização de Banco de Dados. Vamos identificar possíveis dependências parciais e transitivas e propor soluções para alcançar a normalização correta. 

### Contexto do Exercício
Temos uma tabela que armazena informações sobre alunos, disciplinas e notas. O objetivo é identificar se essa tabela está em Primeira Forma Normal (1FN), Segunda Forma Normal (2FN) ou Terceira Forma Normal (3FN), e corrigir quaisquer problemas de dependências parciais ou transitivas para garantir a normalização.

### Passo 1: Verificar Primeira Forma Normal (1FN)
A Primeira Forma Normal (1FN) exige que todos os valores em uma coluna sejam atômicos, ou seja, não podem ser divididos em subconjuntos. Vamos começar examinando a estrutura da tabela para garantir que está em 1FN.

#### Tabela Original
| ID do Aluno | Nome do Aluno | Disciplinas        | Nota     |
|------------|--------------|-------------------|----------|
| 1          | João         | Matemática, Física | 8, 9     |
| 2          | Maria        | Biologia, Química  | 7, 6     |

A tabela acima contém colunas com valores compostos, como "Disciplinas" e "Nota". Para atender à 1FN, precisamos separar esses valores em tabelas distintas.

#### Solução para 1FN
Vamos dividir a tabela original em duas tabelas separadas: uma para alunos e outra para disciplinas e notas. A nova estrutura será a seguinte:

**Tabela de Alunos**
| ID do Aluno | Nome do Aluno |
|------------|--------------|
| 1          | João         |
| 2          | Maria        |

**Tabela de Notas**
| ID do Aluno | Disciplina | Nota |
|------------|------------|------|
| 1          | Matemática | 8    |
| 1          | Física     | 9    |
| 2          | Biologia   | 7    |
| 2          | Química    | 6    |

Agora que a tabela está em 1FN, cada coluna contém valores atômicos.

### Passo 2: Verificar Segunda Forma Normal (2FN)
A Segunda Forma Normal (2FN) exige que todos os atributos não-chave dependam completamente da chave primária. Se uma tabela possui uma chave primária composta, cada atributo não-chave deve depender de todos os componentes dessa chave.

#### Solução para 2FN
Com a tabela de notas acima, a chave primária é composta por "ID do Aluno" e "Disciplina". Como cada nota está associada a um aluno e a uma disciplina, a dependência está correta. Portanto, a tabela já está em 2FN.

### Passo 3: Verificar Terceira Forma Normal (3FN)
A Terceira Forma Normal (3FN) exige que todos os atributos não-chave dependam apenas da chave primária e não tenham dependências transitivas.

#### Solução para 3FN
Na tabela de notas, todos os atributos não-chave (Nota) dependem apenas da chave primária composta ("ID do Aluno" e "Disciplina"). Como não há dependências transitivas, a tabela está em 3FN.

### Conclusão
Ao dividir a tabela original em duas tabelas separadas e corrigir as dependências parciais, alcançamos a normalização até a Terceira Forma Normal (3FN). Isso garante que a estrutura do Banco de Dados seja mais robusta, evitando redundâncias e anomalias de atualização. O próximo passo é testar as operações de leitura, inserção e atualização para garantir que a estrutura normalizada atenda aos requisitos do sistema.