from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from typing_extensions import Concatenate


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for i, page in enumerate(reader.pages):
            content = page.extract_text()
            if content:
                text += content
    return text

def charactersplitter (pdf_path):
    text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap  = 200,
    length_function = len,
    )
    raw_text = extract_text_from_pdf(pdf_path)
    texts = text_splitter.split_text(raw_text)
    
    return texts