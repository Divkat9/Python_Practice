def show_messages(first_message, last_message):
    messages = {'f' : first_message, 'l':last_message}
    return messages

final_message = show_messages('hey', 'there')
print(final_message)

def send_messages():
    for message in final_message:
        print(final_message)
