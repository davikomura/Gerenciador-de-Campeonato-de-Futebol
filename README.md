Para criar um README para o seu GitHub com o código que você compartilhou, você pode seguir este modelo básico:

---

# Brasileirão Simulator

Este é um simulador simples de resultados de jogos de futebol do Campeonato Brasileiro. O código gera resultados aleatórios com base em uma "força" atribuída a cada time e apresenta uma tabela de classificação com base nos resultados simulados.

## Funcionalidades

- Simulação de resultados de jogos do Campeonato Brasileiro.
- Cálculo da tabela de classificação com base nos resultados simulados.

## Uso

1. Defina a "força" de cada time no arquivo `times.csv`.
2. Execute o script `main.py` para simular os resultados.
3. Veja a tabela de classificação gerada no arquivo `output.png`.

## Requisitos

- Python 3.x
- pandas
- numpy
- dataframe_image

## Como executar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script:

   ```bash
   python simulador_campeonato.py
   ```

## Exemplo de saída

![Tabela de Classificação](output_teste.png)
