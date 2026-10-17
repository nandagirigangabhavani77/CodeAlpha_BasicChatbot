print("--- Simple Chatbot ---")
print("Type 'bye' to exit\n")
while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi! How are you?")
    elif user == "how are you":
        print("Bot: I am fine, thank you! How about you?")
    elif user == "what is your name":
        print("Bot: I am a basic Python chatbot.")
    elif user == "what are you doing" or user == "what are you doing?":
        print("Bot: I am chatting with you!")
    elif user == "who created you":
        print("Bot: I was created using Python for my internship project.")
    elif user == "help":
        print("Bot: You can ask me 'hi', 'how are you', 'what is your name', or 'who created you'.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I didn't understand that. Type 'help' to see what you can ask.")