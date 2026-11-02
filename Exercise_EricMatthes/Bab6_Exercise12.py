# Mengembangkan exercise 6.11
cities = {
    "jakarta": {
        "country": "Indonesia", 
        "population": "11000000",
        "language": "indonesian",
        "Famous_place": "Monas"
    },
    "tokyo": {
        "country": "Japan",
        "population": "14000000",
        "language": "japanese",
        "Famous_place": "Tokyo Tower"
    },
    "seoul": {
        "country": "south korea",
        "population": "9400000",
        "language": "korean",
        "Famous_place": "N Seoul Tower"
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Language: {info['language'].title()}")
    print(f"Famous_Place: {info['Famous_place']}")