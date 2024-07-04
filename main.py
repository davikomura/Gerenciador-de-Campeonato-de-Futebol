from championship_management.manage_championship import gerenciar_campeonato
from data_processing.process_data import process_json

def main():
    file_path = 'data.json'
    divisoes = process_json(file_path)
    divisoes = gerenciar_campeonato(divisoes)

if __name__ == "__main__":
    main()
