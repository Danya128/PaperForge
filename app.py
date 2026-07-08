from services.ingestion import fetch_documents, create_chunks, create_embeddings


KNOWLEDGE_BASE = "uploaded_files"
RULES_STYLE_BASE = "writing_rules"
DB_NAME = "vector_db"
DB_RULES = "rules_db"

# Function used for creating a vector database
def process_documents(folder_name, db_name):
    documents = fetch_documents(folder_name)
    chunks = create_chunks(documents)
    vector_store = create_embeddings(chunks, db_name)
    return vector_store
