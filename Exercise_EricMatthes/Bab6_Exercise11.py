cities = {
    "jakarta": {
        "country": "Indonesia", 
        "population": "11000000",
        "fact": "Jakarta is the largest city in Indonesia."
    },
    "tokyo": {
        "country": "Japan",
        "population": "14000000",
        "fact": "Tokyo is the capital of Japan."
    },
    "seoul": {
        "country": "south korea",
        "population": "9400000",
        "fact": "Seoul is the capital of South Korea."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")