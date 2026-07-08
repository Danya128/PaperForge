import os
import glob
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings



load_dotenv(override=True)
MODEL = "gpt-4.1-nano"



# Fetch all PDF docs from folder and return them as LangChain Document Object
def fetch_documents(knowledge_base):
    pdf_files = glob.glob(str(Path(knowledge_base) / "*.pdf"))
    documents = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        documents.extend(loader.load())
    return documents



# Split documents into small chunks for further RAG processing
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = text_splitter.split_documents(documents)
    return chunks


# Convert the chunks into vectors and store them into the vector database
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
def create_embeddings(chunks, db_name):
    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()
    vectorstore = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = db_name
        )
    return vectorstore