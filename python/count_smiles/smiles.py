def count_smiley(arr:list)->int:
    cont=0
    
    for i in arr:
        if i.endswith(':D') or i.endswith(':)') or i.endswith(';-D') or i.endswith(':~)') or i.endswith(';~D'):
           cont +=1 
        
    return cont


print(count_smiley([':D',':~)',';~D',':)']))
