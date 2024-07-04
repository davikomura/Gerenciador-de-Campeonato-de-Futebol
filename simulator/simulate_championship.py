from random import randint
import pandas as pd
import numpy as np
# import dataframe_image as dfi

def resultado(ForcaA, ForcaB):

    espaco = ForcaA + ForcaB

    sorteA = randint(0, ForcaA)
    golA = int(sorteA * ((ForcaA + randint(0, 10 - ForcaB))/espaco))

    sorteB = randint(0, ForcaB)
    golB = int(sorteB * ((ForcaB + randint(0, 10 - ForcaA))/espaco))

    if golA < 0:
        golA = 0

    if golB < 0:
        golB = 0

    return [golA, golB]

def turno(times):
    
    jogos = []
    
    for i in range(len(times)):
        j = i + 1
        while j < len(times):
            A, B = times[i], times[j]
            #p = ("{} x {}".format(A['Time'], B['Time']))
            x = resultado(int(A['Nível']), int(B['Nível']))
            x2 = resultado(int(A['Nível']), int(B['Nível']))
            z = [A['Time'], B['Time']]
            z2 = [A['Time'], B['Time']]
            w = ('{} {} x {} {}'.format(z[0], x[0], x[1], z[1]))
            w2 = ('{} {} x {} {}'.format(z2[0], x2[0], x2[1], z2[1]))
                        
            placar = z + x
            placar2 = z2 + x2
            
            j += 1
            jogos.append(placar)
            jogos.append(placar2)
            
    df = pd.DataFrame(jogos, columns=['Time A', 'Time B', 'Gols Time A', 'Gols Time B'])
    
    conditionlist = [
        (df['Gols Time A']> df['Gols Time B']),
        (df['Gols Time A'] < df['Gols Time B']),
        (df['Gols Time A'] == df['Gols Time B'])]
    choicelist = [df['Time A'], df['Time B'], 'Empate']
    df['Vencedor'] = np.select(conditionlist, choicelist)
    
    df["Placar"] = df['Gols Time A'].map(str) + "x" + df['Gols Time B'].map(str)

    
    return df

def numeroDeVitorias(data, clube):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter = df["Vencedor"] == clube
    return (data[filter]['Vencedor'].count()).astype(np.int64)

def numeroDeJogos(data, clube):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = df["Time A"] == clube
    filter2 = df["Time B"] == clube
    return (data[filter1]["Time A"].count() + data[filter2]["Time B"].count()).astype(np.int64)

def getPoints(data, clube):
    df = data.apply(lambda x: x.strip() if isinstance(x, str) else x)
    filter1 = df["Time A"] == clube
    filter2 = df["Time B"] == clube
    filter3 = df["Vencedor"] == clube
    filter4 = (df["Time A"] == clube) | (df["Time B"] == clube)
    filter5 = df["Vencedor"] == 'Empate'

    v1 = data[(filter1) & (filter3)]
    v1 = v1['Vencedor'].count()
    v2 = data[(filter2) & (filter3)]
    v2 = v2['Vencedor'].count() 
    v3 = data[(filter4) & (filter5)]
    v3 = v3['Vencedor'].count()
    return ((v2*3)+(v1*3)+v3).astype(np.int64)

def numeroDeEmpates(data, clube):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = (df["Time A"] == clube) | (df["Time B"] == clube)
    filter2 = df["Vencedor"] == 'Empate'
    df = data[(filter1) & (filter2)]
    empates = df['Vencedor'].count()
    return empates.astype(np.int64)

def numeroDeDerrotas(data, clube):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1 = (df["Time A"] == clube) | (df["Time B"] == clube)
    filter2 = (df["Vencedor"]!= clube) & (df["Vencedor"] != 'Empate')
    df = data[(filter1) & (filter2)]
    derrotas = df['Vencedor'].count()
    return derrotas.astype(np.int64)

def getGP(data, clube ):
    df = data.apply(lambda x: x.str.strip() if isinstance(x, str) else x)
    filter1  =  df["Time A"] == clube
    filter2  =  df["Time B"] == clube
    df1      =  data[(filter1)]
    df2      =  data[(filter2)]
    placar1  =  df1['Placar'].str.split('x')
    placar2  =  df2['Placar'].str.split('x')

    gp       =  0
    gc       =  0
    for g1, g2 in placar1:
        gp = (gp + pd.to_numeric( g1 ))
        gc = (gc + pd.to_numeric( g2 ))

    for g1, g2 in placar2:
        gp = (gp + pd.to_numeric( g2 )) 
        gc = (gc + pd.to_numeric( g1 ))
    return gp, gc

def tabela(times):

    df = turno(times)
    
    clubs = [x['Time'] for x in times]
    
    cb  =  pd.Series(clubs, name="Times")
    cb  =  cb.to_frame()
    
    dfTable = cb[["Times"]].copy()
    for column in ["PG", "J", "V", "E", "D", "GP", "GC", "SG"]:
        dfTable[column] = 0

    for index, row in dfTable.iterrows():
        c1  =  row['Times']
        c1  =  c1.strip()
        
        pg = getPoints(df, c1)
        j = numeroDeJogos(df, c1)
        v = numeroDeVitorias(df, c1)
        e = numeroDeEmpates(df, c1)
        d = numeroDeDerrotas(df, c1)
        gp, gc = getGP(df, c1)
        
        dfTable.at[index, 'PG'] = pg
        dfTable.at[index, 'J']  = j
        dfTable.at[index, 'V']  = v
        dfTable.at[index, 'E']  = e
        dfTable.at[index, 'D']  = d
        dfTable.at[index, 'GP'] = gp
        dfTable.at[index, 'GC'] = gc
        dfTable.at[index, 'SG'] = gp - gc
        
    dfTable['Times'] = dfTable['Times'].str.capitalize() 
    dfTable = dfTable.sort_values(by=['PG', 'SG', 'V', 'GP'], ascending=False)
    dfTable = dfTable.reset_index(drop=True)
    dfTable.index = pd.RangeIndex(start=1, stop=len(dfTable['Times'])+1, step=1)
    
    return dfTable

# def imagem_df(x, y):
#     df = tabela(x)
#     dfi.export(df, y)