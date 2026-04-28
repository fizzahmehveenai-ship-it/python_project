name = input("Enter your name: ")

print(f"Welcome {name}! 🤖")
print("Ask me: hello, price, location, order, bye")

while True:
    user = input(f"{name}: ").lower()

    if "hello" in user:
        print("Bot: Hello! 😊")

    elif "price" in user:
        print("Bot: Bangles price is 300 PKR")

    elif "location" in user:
        print("Bot: We are in Vehari")

    elif "order" in user:
        print("Bot: Contact: 030XXXXXXX")

    elif "bye" in user:
        print("Bot: Goodbye! ❤️")
        break

    else:
        print("Bot: Try asking something else")