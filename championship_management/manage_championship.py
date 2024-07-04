from simulator.simulate_championship import tabela
import pandas as pd

def gerenciar_campeonato(divisoes):
    # Armazenar as tabelas de cada divisão
    tabelas = []

    # Gerar as tabelas para cada divisão
    for i, divisao in enumerate(divisoes):
        tabela_divisao = tabela(divisao)
        tabelas.append(tabela_divisao)
        print(f"Tabela da Divisão {i+1}:")
        print(tabela_divisao)
        print("\n")

    # Realizar as promoções e rebaixamentos
    for i in range(len(divisoes) - 1):
        rebaixados = tabelas[i].iloc[-4:]['Times'].tolist()
        promovidos = tabelas[i+1].iloc[:4]['Times'].tolist()

        print(f"Rebaixados da Divisão {i+1} para Divisão {i+2}: {rebaixados}")
        print(f"Promovidos da Divisão {i+2} para Divisão {i+1}: {promovidos}")

        # Rebaixar times
        for time in rebaixados:
            for team in divisoes[i]:
                if team['Time'].capitalize() == time:
                    divisoes[i+1].append(team)
                    divisoes[i].remove(team)
                    break

        # Promover times
        for time in promovidos:
            for team in divisoes[i+1]:
                if team['Time'].capitalize() == time:
                    divisoes[i].append(team)
                    divisoes[i+1].remove(team)
                    break

    # Promover da última divisão
    promovidos_ultima_divisao = tabelas[-1].iloc[:4]['Times'].tolist()
    print(f"Promovidos da última divisão (Divisão {len(divisoes)}) para Divisão {len(divisoes)-1}: {promovidos_ultima_divisao}")

    for time in promovidos_ultima_divisao:
        for team in divisoes[-1]:
            if team['Time'].capitalize() == time:
                divisoes[-2].append(team)
                divisoes[-1].remove(team)
                break

    return divisoes
