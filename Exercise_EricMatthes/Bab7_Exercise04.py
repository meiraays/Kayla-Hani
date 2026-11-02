prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    topping = input(prompt)

    if topping.lower() == "quit":
        break

    print (f"I'll add {topping} to your pizza!")