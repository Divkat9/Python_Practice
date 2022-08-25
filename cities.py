city1 = {'name':'lincoln', 'population':'200,000', 'fact':'capital building'}
city2 = {'name':'hyderabad','population':'1000,000', 'fact':'charminar'}
city3 = {'name':'seattle', 'population':'500,000', 'fact':'beach'}
cities = [city1, city2, city3]
for city, population, fact in cities:
    print("f{city}'s population is {population} and they have {fact}")