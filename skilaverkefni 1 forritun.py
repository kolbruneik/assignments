year = int(input("please input number of years ")) 

if year <= 0 :
    print ("invalid input")
else:
    second = 60 * 60 * 24 * 365
    birth = second / 7
    death = second / 13
    immigration = second / 35
    population = 307357870
    populationchange = (birth * year) - (death * year) + (immigration * year)
    newpopulation = population + populationchange
    newpopulation = round(newpopulation)
    print("the new population will be", newpopulation, "in", year, "years")
