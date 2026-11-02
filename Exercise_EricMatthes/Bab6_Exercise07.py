person1 = {
    "first_name": "Kayla",
    "last_name": "Hani",
    "age": 18,
    "city": "Semarang"
}

person2 = {
    "first_name": "Nayla",
    "last_name": "Azka",
    "age": 18,
    "city": "Surakarta"
}

person3 = {
    "first_name": "Muhammad",
    "last_name": "Daffa",
    "age": 19,
    "city": "Surakarta"
}

people = [person1, person2, person3]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")