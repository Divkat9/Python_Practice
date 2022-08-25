rivers = {'nile':'egypt', 'ganges':'india', 'missouri':'usa',}
country = rivers.values()

for river, country in rivers.items():
    print(f"the {river} runs through {country}")