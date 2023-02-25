def people_whit_age_drink(age):
    drinks ={
            '13':'drink tody',
            '17':'drink coke',
            '18':'drink beer',
            '20':'drink beer',
            '30':'drink whisky',
            }

    return drinks[age]


print(people_whit_age_drink(15))
