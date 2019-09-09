import math
year = int(input("Years: ")) 

if year < 0 :
    print ("Invalid input!")
else:
    second = 60 * 60 * 24 * 365
    birth = second / 7
    death = second / 13
    immigration = second / 35
    population = 307357870
    populationchange = (birth * year) - (death * year) + (immigration * year)
    newpopulation = population + populationchange
    newpopulation = math.floor(newpopulation)
    print("New population after" ,year,  "years is" ,newpopulation,)
