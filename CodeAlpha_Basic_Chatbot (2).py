import spacy
nlp = spacy.load('en_core_web_sm')

def preprocess(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

def recognize_intent(text):
    doc = nlp(text)
    if any([token.text.lower() in ['hi', 'hello', 'hey'] for token in doc]):
        return 'greeting'
    elif any([token.text.lower() == 'bye' for token in doc]):
        return 'farewell'
    elif any([token.text.lower() in ['thanks', 'thank'] for token in doc]):
        return 'thanks'
    else:
        return 'unknown'


def generate_response(intent):
    if intent == 'greeting':
        return "Hello! How can I assist you today?"
    elif intent == 'farewell':
        return "Goodbye! Have a great day!"
    elif intent == 'thanks':
        return "You're welcome! Anything else I can help with?"
    else:
        return "I'm sorry, I didn't understand that."

def chatbot():
    print("Chatbot: Hi there! I am your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
        intent = recognize_intent(user_input)
        response = generate_response(intent)
        print(f"Chatbot: {response}")
        if intent == 'farewell':
            break

chatbot()

