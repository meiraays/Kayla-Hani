# while
topping = ""

while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit'): ")

    if topping != "quit":
        print(f"I'll add {topping} to your pizza!")

# active
active = True

while active: 
    topping = input ("Enter a pizza topping (or 'quit'): ")

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza!")

# break
while True:
    topping = input("Enter a pizza topping (or 'quit): ")

    if topping == "quit":
        break
    
    print(f"I'll add {topping} to your pizza!")