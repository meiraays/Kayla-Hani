favorite_languages = {
    "jen": "phyton",
    "sarah": "c",
    "edward": "rust",
    "phil": "phyton"
}

people = ["jen", "kayla", "sarah", "rose", "hihu"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take our poll!")