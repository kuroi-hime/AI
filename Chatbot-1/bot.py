import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def generate_response(user_message):
    try:
        system_instructions = (
            "You're a personal and smart chatbot."
            "Your style is polite, professional, and you answer concisely according to the user's language."
        )

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_instructions},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=150
        )
        
        return completion.choices[0].message.content

    except Exception as e:
        return f"Sorry, a technical error occurred: {str(e)}"

print("The Chatbot is ready to go! Type 'Exit' to end the conversation..")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['exit']:
        bot_reply = generate_response("bye")
        print(f"Chatbot: {bot_reply}")
        break
        
    bot_reply = generate_response(user_input)
    print(f"Chatbot: {bot_reply}")