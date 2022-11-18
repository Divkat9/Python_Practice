"""11-1. City, Country"""
def city_country(city, country):
    """Function which accepts City and Country"""
    city = input("Which City are you from?: ")
    country = input("Which Country is this City in?: ")
    city_country = f'{city}, {country}'
    return city_country.title()