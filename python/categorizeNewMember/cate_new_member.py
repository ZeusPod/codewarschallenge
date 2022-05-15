def open_or_senior(data:int):
    large=len(data)
    title = []
    for i in range(large):
        if data[i][0] >= 55 and data[i][1] > 7:
            title.append('Senior')
        else: 
            title.append('Open')    

    return title


