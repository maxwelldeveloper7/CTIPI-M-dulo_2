**Aula 23-24: Normalização em Banco de Dados - Primeira a Terceira Forma Normal**

*Refinando a Estrutura dos Dados*

Nesta aula, embarcaremos em uma jornada pela normalização em Banco de Dados, uma técnica essencial para organizar e otimizar a estrutura dos dados. Vamos explorar desde a Primeira até a Terceira Forma Normal, entendendo os princípios e aplicando-os em exemplos práticos.

**1. Primeira Forma Normal (1FN): Eliminação da Repetição**

A Primeira Forma Normal estabelece que cada coluna em uma tabela de Banco de Dados deve conter apenas valores atômicos, ou seja, valores indivisíveis. Isso elimina a repetição de grupos de valores em uma mesma coluna.

*Ilustração: Exemplo de Primeira Forma Normal*

![Primeira Forma Normal](link_para_imagem1)

Por exemplo, suponha que tenhamos uma tabela de pedidos onde uma única coluna contém vários itens separados por vírgula. Para normalizar para a 1FN, precisamos dividir esses itens em linhas individuais, garantindo que cada célula contenha apenas um valor.

**2. Segunda Forma Normal (2FN): Eliminação de Dependências Parciais**

A Segunda Forma Normal requer que uma tabela esteja na 1FN e que cada não-chave dependa totalmente da chave primária, eliminando dependências parciais. Isso significa que cada atributo não-chave deve depender diretamente da chave primária, e não de parte dela.

*Ilustração: Exemplo de Segunda Forma Normal*

![Segunda Forma Normal](link_para_imagem2)

Por exemplo, em uma tabela de pedidos com atributos como número do pedido, produto e preço, se o preço depender apenas do número do pedido e não do produto, temos uma dependência parcial. Para normalizar para a 2FN, precisamos dividir esses atributos em tabelas separadas.

**3. Terceira Forma Normal (3FN): Eliminação de Dependências Transitivas**

A Terceira Forma Normal exige que uma tabela esteja na 2FN e que não haja dependências transitivas entre os atributos, ou seja, nenhum atributo não-chave deve depender de outro atributo não-chave.

*Ilustração: Exemplo de Terceira Forma Normal*

![Terceira Forma Normal](link_para_imagem3)

Por exemplo, em uma tabela de funcionários com atributos como número do funcionário, departamento e gerente, se o departamento determina quem é o gerente, temos uma dependência transitiva. Para normalizar para a 3FN, precisamos remover essa dependência movendo o atributo de gerente para uma tabela separada.

**Conclusão: Refinando a Estrutura dos Dados**

A normalização em Banco de Dados é essencial para garantir a eficiência, integridade e consistência dos dados. Ao entender e aplicar os princípios da Primeira à Terceira Forma Normal, podemos criar estruturas de dados bem organizadas e adaptáveis, preparadas para lidar com os desafios do mundo real. Nos próximos encontros, exploraremos formas ainda mais avançadas de normalização e técnicas para otimizar o desempenho dos Bancos de Dados.

**Atividade Avaliativa - Aula 23-24: Normalização em Banco de Dados - Primeira a Terceira Forma Normal**

*Instruções: Escolha a alternativa correta para cada pergunta.*

1. **O que estabelece a Primeira Forma Normal (1FN) em Banco de Dados?**
   a) Cada coluna em uma tabela deve conter apenas valores numéricos.
   b) Cada coluna em uma tabela deve conter apenas valores atômicos, eliminando a repetição de grupos de valores.
   c) A tabela deve ter uma chave estrangeira que referencia outra tabela.
   d) A tabela deve ser dividida em múltiplas tabelas para evitar a redundância de dados.

2. **Qual é o objetivo principal da Segunda Forma Normal (2FN) em um Banco de Dados?**
   a) Eliminar dependências transitivas entre os atributos.
   b) Garantir que cada atributo não-chave dependa diretamente da chave primária, eliminando dependências parciais.
   c) Garantir que cada atributo seja único em uma tabela.
   d) Organizar os dados em tabelas separadas para facilitar a consulta.

3. **O que a Terceira Forma Normal (3FN) exige em um Banco de Dados?**
   a) Cada coluna em uma tabela deve conter apenas valores atômicos.
   b) Eliminar dependências parciais entre os atributos.
   c) Garantir que não haja dependências transitivas entre os atributos, ou seja, nenhum atributo não-chave deve depender de outro atributo não-chave.
   d) Organizar os dados em uma única tabela para simplificar a estrutura.

4. **Por que a normalização em Banco de Dados é importante?**
   a) Para aumentar a redundância de dados e melhorar o desempenho.
   b) Para complicar a estrutura dos dados e dificultar a manutenção.
   c) Para garantir a eficiência, integridade e consistência dos dados.
   d) Para diminuir a segurança dos dados e aumentar os riscos de perda.

5. **Qual é o resultado final da normalização em Banco de Dados?**
   a) Uma estrutura de dados altamente redundante.
   b) Uma estrutura de dados simplificada e mais fácil de manter.
   c) Uma estrutura de dados complexa que dificulta a consulta.
   d) Uma estrutura de dados sem nenhuma relação entre as tabelas.

**Gabarito:**
1. b) Cada coluna em uma tabela deve conter apenas valores atômicos, eliminando a repetição de grupos de valores.
2. b) Garantir que cada atributo não-chave dependa diretamente da chave primária, eliminando dependências parciais.
3. c) Garantir que não haja dependências transitivas entre os atributos, ou seja, nenhum atributo não-chave deve depender de outro atributo não-chave.
4. c) Para garantir a eficiência, integridade e consistência dos dados.
5. b) Uma estrutura de dados simplificada e mais fácil de manter.