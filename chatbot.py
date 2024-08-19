from dotenv import load_dotenv
import os
# from openai import OpenAI
from pdf_extract import charactersplitter 
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from typing_extensions import Concatenate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)


def chat_with_gpt(prompt, pdf_content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": f"You are a helpful assistant that answers questions based on the following book content:\n\n{pdf_content}"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with GPT: {e}"

if __name__ == "__main__":
    pdf_path = r"E:\CV\Muhammad Hamza.pdf"
    pdf_content = extract_text_from_pdf(pdf_path)
    
    if pdf_content:
        print("PDF text extraction successful. The chatbot is now ready to answer questions based on the book content.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                break
            
            response = chat_with_gpt(user_input, pdf_content)
            print("Chatbot: ", response)
    else:
        print("Failed to extract text from the PDF. Exiting.")