def whatday(day):
    days = {
            1:'Sunday',
            2:'Monday',
            3:'Tuesday',
            4:'Wednesday',
            5:'Thursday',
            6:'Friday',
            7:'Saturday'

            }
    if day >= 8 or day<= 0:
        return 'Wrong, please enter a number between 1 and 7'
    else:
        return days[day]

print(whatday(5))
