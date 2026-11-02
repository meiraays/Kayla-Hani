def city_country(city, country="Indonesia"):
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))
print(city_country("jakarta", "indonesia"))
print(city_country("tokyo", "japan"))