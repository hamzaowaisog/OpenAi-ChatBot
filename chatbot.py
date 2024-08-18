from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [{
            "role": "user",
            "content": prompt
        }]
        
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
        while True:
            user_input = input("You: ")
            if user_input.lower() in  ["exit","quit","bye"]:
                break
            
            response = chat_with_gpt(user_input)
            print("Chatbot: ", response)

