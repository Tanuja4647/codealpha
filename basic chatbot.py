def greet():
    print("Hi there! I'm a basic chatbot. How can I assist you today?")

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How are you?"

    elif 'how are you' in user_input:
        return "I'm just a chatbot, but thanks for asking!"

    elif 'bye' in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that. Can you ask something else?"

def chat():
    greet()
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
chat()