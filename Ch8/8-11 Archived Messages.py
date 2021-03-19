messages_list = ["Hello", "How are you?", ":)"]
sent_messages = []

def print_messages(messages):
    for message in messages:
        print(message)

def send_messages(send_messages):
    while send_messages:
        send_message = send_messages.pop()
        sent_messages.append(send_message)
    print(sent_messages)

print_messages(messages_list)
send_messages(messages_list[:])
print_messages(messages_list)