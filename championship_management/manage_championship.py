from simulator.simulate_championship import standings
import pandas as pd

def manage_championship(divisions):
    # Store tables for each division
    tables = []

    # Generate tables for each division
    for i, division in enumerate(divisions):
        division_table = standings(division)
        tables.append(division_table)
        print(f"Table of Division {i+1}:")
        print(division_table)
        print("\n")

    # Perform promotions and relegations
    for i in range(len(divisions) - 1):
        relegated_teams = tables[i].iloc[-4:]['Teams'].tolist()
        promoted_teams = tables[i+1].iloc[:4]['Teams'].tolist()

        print(f"Relegated from Division {i+1} to Division {i+2}: {relegated_teams}")
        print(f"Promoted from Division {i+2} to Division {i+1}: {promoted_teams}")

        # Relegate teams
        for team_name in relegated_teams:
            for team in divisions[i]:
                if team['Team'].capitalize() == team_name:
                    divisions[i+1].append(team)
                    divisions[i].remove(team)
                    break

        # Promote teams
        for team_name in promoted_teams:
            for team in divisions[i+1]:
                if team['Team'].capitalize() == team_name:
                    divisions[i].append(team)
                    divisions[i+1].remove(team)
                    break

    # Promote from the last division
    promoted_from_last_division = tables[-1].iloc[:4]['Teams'].tolist()
    print(f"Promoted from the last division (Division {len(divisions)}) to Division {len(divisions)-1}: {promoted_from_last_division}")

    for team_name in promoted_from_last_division:
        for team in divisions[-1]:
            if team['Team'].capitalize() == team_name:
                divisions[-2].append(team)
                divisions[-1].remove(team)
                break

    return divisions
