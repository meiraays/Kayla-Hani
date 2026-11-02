pet1 = {
    "name": "Bibu",
    "animal": "cat",
    "owner": "Kayla"
}

pet2 = {
    "name": "Hihu",
    "animal": "rabbit",
    "owner": "Nayla"
}

pet3 = {
    "name": "Miu",
    "animal": "Cat",
    "owner": "Daffa"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Name: {pet['name']}")
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}\n")