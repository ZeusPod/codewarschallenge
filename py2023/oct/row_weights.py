def row_weights(array):
   first_team = sum(array[i] for i, _ in enumerate(array) if i % 2 == 0)
   second_team = sum(array[i] for i, _ in enumerate(array) if i % 2 == 1)
   return(first_team, second_team)



print(row_weights([80])) 
