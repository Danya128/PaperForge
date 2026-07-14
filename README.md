# Paper Forge
### AI-powered academic writing assistant that generates assignments referenced assignments from user-uploaded documents, using Retrieval-Augmented Generation (RAG), LangChain, ChromaDB, OpenAI, and Streamlit


## Main Features
### The main feature of PaperForge is its ability to generate assignments that reference the documents uploaded by the user. Unlike general-purpose AI assistants, which often produce unsupported content or omit citations entirely, PaperForge retrieves information from the uploaded sources and includes appropriate in-text citations and references according to the selected referencing style


## How it works
### 1. Users enter relevant information about the text they want
### 2. User uploads PDF documents
### 3. Once the button is pressed, the documents(style formatting rules and user's uploads) are split into chunks
### 4. Chunks converted into embeddings(vercors)
### 5. The vectors are stored in a vector database
### 6. Relevant chunks are retrieved
### 7. Writing style rules are retrieved
### 8. The system generates the assignment using both retrieved documents for writing references


## Capabilities
### -- Accept one or multiple documents
### -- Retrieve relevant information using RAG
### -- Rather than copy and paste text from documents, it generates a unique assignment
### -- Support multiple referencing styles
### -- Write properly formatted references
### -- Include a simple Streamlit interface
### -- Possibility to adjust the number of words to generate


## Demo
[Watch the PaperForge demo](https://youtu.be/VtGKT3n1KWo?si=QDQxzoafct27tf3S)
