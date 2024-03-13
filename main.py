import nltk
import random
from nltk.chat.util import Chat, reflections
import patterns
import reflections

# Create a Chat object
chatbot = Chat(patterns.patterns, reflections.reflections)

# Define a function to start the conversation
def chat():
    print("Hello")
    print("Welcome! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "quit":
            break

# Start the conversation
if __name__ == "__main__":
    chat()
