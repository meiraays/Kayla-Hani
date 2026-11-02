# nama-nama sungai dan negara
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "kapuas": "indonesia",
}

# Menampilkan nama sungai dan negara
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Menampilkan nama sungai saja
print ("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Menampilkan nama negara saja
print("\nCountries")
for country in rivers.values():
    print(country.title())