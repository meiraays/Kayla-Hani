# Perbandingan string
food = "pizza"
print(food == "pizza")  # True
print(food != "pizza")  # False

# Menggunakan Lower ()
name = "KAYLA"
print(name.lower() == "kayla")  # True
print(name.lower() == "hani")  # False

# Perbandingan angka
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age > 15)   # True
print(age < 15)   # False
print(age >= 18)  # True
print(age <= 15)  # False

# Menggunakan and dan or
print(age > 15 and age < 20)  # True
print(age > 20 and age < 25)  # False
print(age > 15 or age > 20)   # True
print(age < 15 or age > 20)   # False

# Menggunakan in dan nor in
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)    # True
print("grape" in fruits)    # False
print("grape" not in fruits) # True
print("apple" not in fruits) # False