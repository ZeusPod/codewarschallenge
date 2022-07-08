def better_than_average(class_points, your_points):
    avg = sum(class_points) / len(class_points)
    if avg < your_points:
        return True 
    else:
        return False 
