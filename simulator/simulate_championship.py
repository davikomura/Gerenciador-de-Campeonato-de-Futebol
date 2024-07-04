from random import randint
import pandas as pd
import numpy as np
# import dataframe_image as dfi

def result(StrengthA, StrengthB):
    space = StrengthA + StrengthB

    # Generate random goals based on team strengths
    randA = randint(0, StrengthA)
    goalsA = int(randA * ((StrengthA + randint(0, 10 - StrengthB)) / space))

    randB = randint(0, StrengthB)
    goalsB = int(randB * ((StrengthB + randint(0, 10 - StrengthA)) / space))

    # Ensure goals are non-negative
    if goalsA < 0:
        goalsA = 0
    if goalsB < 0:
        goalsB = 0

    return [goalsA, goalsB]

def round(teams):
    games = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            teamA, teamB = teams[i], teams[j]

            # Simulate two games between each pair of teams
            result1 = result(int(teamA['Level']), int(teamB['Level']))
            result2 = result(int(teamA['Level']), int(teamB['Level']))

            # Format results
            game1 = [teamA['Team'], teamB['Team']] + result1
            game2 = [teamA['Team'], teamB['Team']] + result2

            games.append(game1)
            games.append(game2)

    # Create DataFrame with game results
    df = pd.DataFrame(games, columns=['Team A', 'Team B', 'Goals Team A', 'Goals Team B'])

    # Determine winners and add to DataFrame
    conditions = [
        (df['Goals Team A'] > df['Goals Team B']),
        (df['Goals Team A'] < df['Goals Team B']),
        (df['Goals Team A'] == df['Goals Team B'])
    ]
    choices = [df['Team A'], df['Team B'], 'Draw']
    df['Winner'] = np.select(conditions, choices)

    # Create string representation of scores
    df["Score"] = df['Goals Team A'].map(str) + "x" + df['Goals Team B'].map(str)

    return df

def numberOfWins(data, club):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter = df["Winner"] == club
    return (data[filter]['Winner'].count()).astype(np.int64)

def numberOfGames(data, club):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = df["Team A"] == club
    filter2 = df["Team B"] == club
    return (data[filter1]["Team A"].count() + data[filter2]["Team B"].count()).astype(np.int64)

def getPoints(data, club):
    df = data.apply(lambda x: x.strip() if isinstance(x, str) else x)
    filter1 = df["Team A"] == club
    filter2 = df["Team B"] == club
    filter3 = df["Winner"] == club
    filter4 = (df["Team A"] == club) | (df["Team B"] == club)
    filter5 = df["Winner"] == 'Draw'

    wins_as_team_a = data[(filter1) & (filter3)]
    wins_as_team_b = data[(filter2) & (filter3)]
    draws = data[(filter4) & (filter5)]

    points = (wins_as_team_a['Winner'].count() * 3) + (wins_as_team_b['Winner'].count() * 3) + draws['Winner'].count()
    return points.astype(np.int64)

def numberOfDraws(data, club):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = (df["Team A"] == club) | (df["Team B"] == club)
    filter2 = df["Winner"] == 'Draw'
    df = data[(filter1) & (filter2)]
    draws = df['Winner'].count()
    return draws.astype(np.int64)

def numberOfLosses(data, club):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = (df["Team A"] == club) | (df["Team B"] == club)
    filter2 = (df["Winner"] != club) & (df["Winner"] != 'Draw')
    df = data[(filter1) & (filter2)]
    losses = df['Winner'].count()
    return losses.astype(np.int64)

def getGoalsForAndAgainst(data, club):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = df["Team A"] == club
    filter2 = df["Team B"] == club
    team_as_a = data[(filter1)]
    team_as_b = data[(filter2)]
    scores_as_a = team_as_a['Score'].str.split('x')
    scores_as_b = team_as_b['Score'].str.split('x')

    goals_for = 0
    goals_against = 0

    for g1, g2 in scores_as_a:
        goals_for += pd.to_numeric(g1)
        goals_against += pd.to_numeric(g2)

    for g1, g2 in scores_as_b:
        goals_for += pd.to_numeric(g2)
        goals_against += pd.to_numeric(g1)

    return goals_for, goals_against

def standings(teams):
    df = round(teams)
    
    # Create DataFrame with team names
    clubs = [x['Team'] for x in teams]
    clubs_series = pd.Series(clubs, name="Teams")
    clubs_df = clubs_series.to_frame()
    
    # Initialize DataFrame for standings
    dfTable = clubs_df[["Teams"]].copy()
    dfTable["Points"] = 0
    dfTable["Games Played"] = 0
    dfTable["Wins"] = 0
    dfTable["Draws"] = 0
    dfTable["Losses"] = 0
    dfTable["Goals For"] = 0
    dfTable["Goals Against"] = 0
    dfTable["Goal Difference"] = 0

    # Fill in standings data for each team
    for index, row in dfTable.iterrows():
        club = row['Teams'].strip()
        
        points = getPoints(df, club)
        games_played = numberOfGames(df, club)
        wins = numberOfWins(df, club)
        draws = numberOfDraws(df, club)
        losses = numberOfLosses(df, club)
        goals_for, goals_against = getGoalsForAndAgainst(df, club)
        goal_difference = goals_for - goals_against
        
        dfTable.at[index, 'Points'] = points
        dfTable.at[index, 'Games Played'] = games_played
        dfTable.at[index, 'Wins'] = wins
        dfTable.at[index, 'Draws'] = draws
        dfTable.at[index, 'Losses'] = losses
        dfTable.at[index, 'Goals For'] = goals_for
        dfTable.at[index, 'Goals Against'] = goals_against
        dfTable.at[index, 'Goal Difference'] = goal_difference

    # Format team names and sort by points, goal difference, wins, and goals scored
    dfTable['Teams'] = dfTable['Teams'].str.capitalize()
    dfTable = dfTable.sort_values(by=['Points', 'Goal Difference', 'Wins', 'Goals For'], ascending=False)
    dfTable = dfTable.reset_index(drop=True)
    dfTable.index = pd.RangeIndex(start=1, stop=len(dfTable['Teams']) + 1, step=1)
    
    return dfTable

# def image_df(x, y):
#     df = standings(x)
#     dfi.export(df, y)