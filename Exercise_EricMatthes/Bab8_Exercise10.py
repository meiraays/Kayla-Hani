def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Hello, how are you?",
    "I'm learning Python programming.",
    "Functions are really useful!",
    "Halo apakabar?"
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("]\nOriginal messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)