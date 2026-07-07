import os
import glob
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv(override=True)
MODEL = "gpt-4.1-nano"


# Fetch all PDF docs from folder and return them as LangChain Document Object
def fetch_documents(knowledge_base):
    folders = glob.glob(str(Path(knowledge_base) / "*"))
    document = []
    for folder in folders:
        loader = DirectoryLoader(
            folder, glob="**/*.pdf", loader_cls=PyPDFLoader, loader_kwargs={"encoding": "utf-8"}
        )
        folder_docs = loader.load()
        for doc in folder_docs:
            document.append(doc)
    return document



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