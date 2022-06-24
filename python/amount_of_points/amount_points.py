
""""
definir una funcion que reciba pares de 10 pares de puntuaciones y devuelva el total de puntos
segun los siguientes criterios:
    1. si x >  y: 3 puntos
    2. si x == y: 1 punto
    3. si x <  y: 0 puntos
hay 10 partidos en el campeonato
"""

import doctest


def points(games):
    dict_games = {}
    for game in games:
        dict_games[game[0]] = game[1]
    
    return dict_games


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
