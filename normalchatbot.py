import random

# Define bot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
}

# Define function to get bot response
def get_response(message):
    message = message.lower()  # Convert message to lowercase
    for key in responses:
        if message in key:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

# Main function to interact with the bot
def main():
    print("Bot: Hi! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot:", get_response(user_input))
            break
        print("Bot:", get_response(user_input))

if __name__ == "__main__":
    main()
