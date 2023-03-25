def bouncing_ball(h, bounce, window):
   result = 1 
   if (h * bounce) > result:
       result += (h * bounce)/window + 1
       return round(result) 
   else:
       return result



print(bouncing_ball(2,0.5,1))
print(bouncing_ball(3,0.66,1.5))
print(bouncing_ball(30,0.66,1.5))
print(bouncing_ball(30, 0.75, 1.5))

