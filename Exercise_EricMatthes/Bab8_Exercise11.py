def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


text_messages = [
    "Hello, how are you?",
    "Good morning!",
    "Have a nice day!",
    "See you tomorrow!"
]

sent_messages = []

send_messages(text_messages[:], sent_messages)

print("\nOriginal messages:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)