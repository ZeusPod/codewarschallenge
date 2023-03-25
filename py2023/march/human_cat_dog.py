def human_years_cat_dog(human_years):
    cats = {
            1:15,
            2:+9,
            3:+4,
            }

    dogs = {
            1:15,
            2:+9,
            3:+5,
            }

    if human_years == 1:
        return [human_years, cats[human_years], dogs[human_years]]
    elif human_years == 2:
        return [human_years, cats[human_years] + 15, dogs[human_years] + 15]
    else:
        animalYears = human_years - 2
        return [human_years, cats[3]*animalYears + 24, dogs[3]*animalYears + 24]



print(human_years_cat_dog(10))
