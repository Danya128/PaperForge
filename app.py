from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.messages import SystemMessage, HumanMessage

MODEL = "gpt-4.1-nano"
DB_NAME = "vector_db"
DB_RULES = "rules_db"

SYSTEM_PROMPT_TEMPLATE = """
You are an expert academic writing assistant.
Your task is to write complete assignments for students.
Instructions:
1. Write about {description}
2. The size of the text must be approximately {no_words}
3. Use the {ref_style} referencing style
4. Follow the referencing and formatting rules provided in: {rules_context}

Use the uploaded reference documents below as your main information source:
{uploads_context}

Requirements:
1. Use the only information supported by the uploads
2. Do not make up facts or citations
3. Include in-text citations whenever is appropriate
4. Follow the writing and referencing style rules
5. Organize the assignment in paragraphs with logical flow
6. Write in a formal academic tone
"""


load_dotenv(override = True)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


vectorstore_uploads = Chroma(persist_directory = DB_NAME, embedding_function = embeddings)
vectorstore_rules = Chroma(persist_directory = DB_RULES, embedding_function = embeddings)


retriever_uploads = vectorstore_uploads.as_retriever()
retriever_rules = vectorstore_rules.as_retriever()

llm = ChatOpenAI(temperature = 0, model_name = MODEL)


def answer_question(description, no_words, ref_style):
    doc_rules = retriever_rules.invoke(f"Tell me about {ref_style} referencing style")
    doc_uploads = retriever_uploads.invoke(f"Give me all relevant information about {description}")
    rules_context = "\n\n".join(doc.page_content for doc in doc_rules)
    uploads_context = "\n\n".join(doc.page_content for doc in doc_uploads)
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(description = description, no_words = no_words, ref_style = ref_style, rules_context = rules_context, uploads_context = uploads_context)
    user_prompt = "Generate the assignment according to the instructions."
    response = llm.invoke([SystemMessage(content = system_prompt), HumanMessage(content = user_prompt)])
    return response.content