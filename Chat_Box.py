import time

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! What's up?",
    "how are you": "I'm good, thanks! How are you?",
    "name": "I'm your Python Chatbot.",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!"
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Sorry, I don't understand that."

def main():
    print("CHATBOX BOT")
    print("Type 'bye' to exit\n")

    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Chatbot: Bye! Take care 😊")
            break

        reply = get_response(user)
        time.sleep(0.5)
        print("Chatbot:", reply)
        print()

if __name__ == "__main__":
    main()
