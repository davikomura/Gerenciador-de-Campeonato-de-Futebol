import json
from simulator.simulate_championship import tabela

def process_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Organizar os times por nível em cada sessão
    for sessao in data:
        data[sessao] = sorted(data[sessao], key=lambda x: int(x['Nível']), reverse=True)
    
    # Criar uma lista de listas com os times de cada sessão
    divisoes = list(data.values())
    
    return divisoes
