# Brasileirão Simulator

Este é um simulador simples de resultados de jogos de futebol do Campeonato Brasileiro. O código gera resultados aleatórios com base em uma "força" atribuída a cada time e apresenta uma tabela de classificação com base nos resultados simulados.

## Funcionalidades

- Simulação de resultados de jogos do Campeonato Brasileiro.
- Cálculo da tabela de classificação com base nos resultados simulados.

## Estrutura do Projeto

- `simulador_campeonato.py`: Contém as funções para simulação de resultados e cálculo da tabela de classificação.
- `teste.py`: Arquivo de teste para importar e executar o simulador de campeonato.

## Requisitos

- Python 3.x
- pandas
- numpy
- dataframe_image

## Como usar

1. Defina a "força" de cada time no arquivo `simulador_campeonato.py`.
2. Execute o script `teste.py` para simular os resultados.
3. Veja a tabela de classificação gerada no arquivo `output.png`.

## Executando o Simulador

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script de teste:

   ```bash
   python teste.py
   ```

## Exemplo de saída

![Tabela de Classificação](output_test.png)
