messages = ['おはよう','こんにちは','こんばんは','さようなら']
sent_messages = []

def send_messages(messages,sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"{current_message}を送っています。")
        sent_messages.append(current_message)

send_messages(messages,sent_messages)
print("\n")
print(messages)
print("\n")
print(sent_messages)