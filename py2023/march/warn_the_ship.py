def warn_the_sheep(queue):
    if wolf_position.index('wolf'):
        wolf_position = (queue[::-1])
        sheep = (wolf_position.index('wolf') +1) -1  
        return f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!'        
    else:
        return 'Pls go away and stop eating my sheep'
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
