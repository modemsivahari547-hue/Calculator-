print("Chatbot: Hello! Type 'bye' to exit")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Chatbot: Hi!")
    elif user.lower() == "how are you":
        print("Chatbot: I am fine!")
    elif user.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: I don't understand")
