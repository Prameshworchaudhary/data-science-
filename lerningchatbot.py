class ChatBot:
    def __init__(self):
        self.responses = {'hi': 'Hello!', 'how are you': 'I am fine, thank you!', 'bye': 'Goodbye!'}
        self.learned_responses = {}

    def get_response(self, message):
        message = message.lower()
        if message in self.responses:
            return self.responses[message]
        elif message in self.learned_responses:
            return self.learned_responses[message]
        else:
            return "I'm sorry, I don't understand that."

    def learn_response(self, message, response):
        message = message.lower()
        self.learned_responses[message] = response

def main():
    bot = ChatBot()
    print("Bot: Hi! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot:", bot.get_response(user_input))
            break
        elif user_input.lower() == 'learn':
            message = input("Enter a message to learn: ")
            response = input("Enter the response: ")
            bot.learn_response(message, response)
            print("Bot: Thank you for teaching me!")
        else:
            print("Bot:", bot.get_response(user_input))

if __name__ == "__main__":
    main()
