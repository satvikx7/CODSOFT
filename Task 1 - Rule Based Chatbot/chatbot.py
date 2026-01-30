def chatbot():
    print("Hello! This is a simple chatbot")
    print("Type bye to stop chatting")

    while True:
        user = input("You: ")
        user = user.lower()

        if user == "hello":
            print("Chatbot: Hi")

        elif user == "hi":
            print("Chatbot: Hello")

        elif user == "how are you":
            print("Chatbot: I am fine")

        elif user == "what is your name":
            print("Chatbot: My name is Chatbot")

        elif user == "bye":
            print("Chatbot: Bye bye")
            break

        else:
            print("Chatbot: Sorry I do not understand")

# calling function
chatbot()
