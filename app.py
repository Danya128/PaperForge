from services.ingestion import fetch_documents, create_chunks, create_embeddings


KNOWLEDGE_BASE = "uploaded_files"
DB_NAME = "vector_db"

def process_documents():
    documents = fetch_documents(KNOWLEDGE_BASE)
    chunks = create_chunks(documents)
    vector_store = create_embeddings(chunks, DB_NAME)
    return vector_store