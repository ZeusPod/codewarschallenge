#debemos comprobar que efectivamente sean 10 minutos (10 instrucciones) y que las mismas regresan al lugar de salida


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
            return True
        else:
            return False    



print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))


 
