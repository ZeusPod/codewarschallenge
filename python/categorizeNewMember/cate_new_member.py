def open_or_senior(data:int):
    """_summary_: funtion for classify if member is senior or open

    Args:
        data (int):list of pair of age and handicap of members

    Returns:
        list: list of clasification of member 
    """    
    large=len(data)
    title = []
    for i in range(large):
        if data[i][0] >= 55 and data[i][1] > 7:
            title.append('Senior')
        else: 
            title.append('Open')    

    return title


