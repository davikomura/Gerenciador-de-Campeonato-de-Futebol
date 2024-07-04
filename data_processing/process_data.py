import json

def process_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Sort teams by level in each session
    for session in data:
        data[session] = sorted(data[session], key=lambda x: int(x['Level']), reverse=True)
    
    # Create a list of lists with teams for each session
    divisions = list(data.values())
    
    return divisions
