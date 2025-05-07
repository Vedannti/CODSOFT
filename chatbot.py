import random
import time

greetings = ["Hello there!How can I assist you?","Hi! What can I do for you todat?","Hey, how can Ihelp you?"]
farewalls = ["Goodbye! Take care!", "See you later!", "Bye! Have a great day!"]
how_are_you = ["I'm doing great, thanks for asking!", "I'm functioning properly!","Everything is running smoothly!"]
study_tips = [
    "Break study sessions into smaller chunks for better focus.",
    "Take 5-10 minutes breaks every hour to stay refreshed.",
    "Use active recall and spaced repetition for better retention.",
    "Study in quiet and distraction free environment."
]

def simulate_typing(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return random.choice(greetings)

    elif "your name" in user_input:
        return "I'm a chatbot built to help you with your questions!"

    elif "how are you" in user_input:
        return random.choice(how_are_you)

    elif "study" in user_input or "how to study" in user_input:
        return random.choice(study_tips)

    elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
        return random.choice(farewalls)

    else:
        return "I'm sorry,I didin't quite understand that. Could you please rephraser?"

def chatbot():
        simulate_typing("Chatbot: Hello! Type 'bye' anytime to end the chat.\n")
        while True:
            user_input = input("You:")
            response = get_response(user_input)
            simulate_typing(f"Chatbot: {response}")
            if any(word in user_input.lower() for word in ["bye","goodbye","See you"]):
                break

chatbot()