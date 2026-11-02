favorite_places = {
    "kayla": ["Semarang", "Jakarta"],
    "nayla": ["Surakarta", "Bandung"],
    "aan": ["Magelang", "Salatiga"]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"- {place.title()}")