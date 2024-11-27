import random
import nltk

# Download NLTK resources
nltk.download('punkt')

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great, thank you!", "I'm just a bot, but I'm functioning well!", "All systems are go!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand that. Can you rephrase?"]
}

# Function to find a response
def get_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase
    for key in responses.keys():
        if key in user_input:  # Check if the keyword exists in the input
            return random.choice(responses[key])
    return random.choice(responses["default"])  # Default response for unmatched inputs

# Chat loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start chatbot
chatbot()
