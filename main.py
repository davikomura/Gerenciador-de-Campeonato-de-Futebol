from championship_management.manage_championship import manage_championship
from data_processing.process_data import process_json

def main():
    file_path = 'data/data.json'
    divisions = process_json(file_path)
    divisions = manage_championship(divisions)

if __name__ == "__main__":
    main()
