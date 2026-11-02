def make_shirt(size = "L", message = "I love Python"):
    print(f"The shirt size is {size} and the message is '{message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with custom message
make_shirt(size="M")

# Shirt of any size with custom message
make_shirt(size="S", message="Python halo!")