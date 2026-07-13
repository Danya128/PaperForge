from services.utils import process_documents
from app import answer_question

import streamlit as st
import os
import glob

output = ""

KNOWLEDGE_BASE = "uploaded_files"
RULES_STYLE_BASE = "writing_rules"
DB_NAME = "vector_db"
DB_RULES = "rules_db"


# Create the writing rules data base
# Using if because st reruns the script on every iteration
if not os.path.exists("rules_db"):
    process_documents(RULES_STYLE_BASE, DB_RULES)

st.markdown("<h1 style='margin-top:-5%;'>PaperForge</h1>", unsafe_allow_html=True)
st.markdown(
    "<h5 style='margin-bottom:5%; margin-top:-2%;'>Your AI study buddy — because deadlines don’t negotiate</h5>",
    unsafe_allow_html=True
)


col1, spacer1, col2, spacer2, col3 = st.columns([3, 0.3, 2.5, 0.3, 4])



# --- upload files --- #
with col2:
    st.markdown(
        "<h5 style='margin-top:15%; margin-bottom:5%;'>Reference documents</h5>",
        unsafe_allow_html=True
    )

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
    
    # upload files into "uploaded_files" folder
    if uploaded_files:
        for file in uploaded_files:
            save_path = os.path.join(KNOWLEDGE_BASE, file.name)
            
            with open(save_path, "wb") as f:
                f.write(file.getbuffer())
                
    # clean "uploaded_files" folder if user wish so
    if not uploaded_files:
        for file in glob.glob("uploaded_files/*pdf"):
            os.remove(file)



# ---  clarify the content --- #
with col1:
    st.markdown(
        "<h5 style='margin-top:15%; margin-bottom:5%;'>Assignment settings</h5>",
        unsafe_allow_html=True
    )

    description = st.text_input("Title and brief description")
    no_words = st.text_input("Number of words")
    ref_style = st.text_input("Referencing style")

    if st.button("Run the process"):
        if not description.strip():
            st.error("Please enter an assignment description")
        elif not no_words.isdigit():
            st.error("Number of words must be a number")
        elif int(no_words) <= 0:
            st.error("Number of words must be greater than 0")
        elif not ref_style.strip():
            st.error("Please enter a referencing style")
        elif not uploaded_files:
            st.error("Please upload at least one PDF document")
        else:
            vectorstore = process_documents(KNOWLEDGE_BASE, DB_NAME)
            output = answer_question(description, no_words, ref_style)



# --- display results --- #
with col3:
    st.markdown(
        "<h5 style='margin-top:10%; margin-bottom:2%;'>Generated assignment</h5>",
        unsafe_allow_html=True
    )

    st.text_area(
        "",
        value = output,
        height = 380,
        disabled = True
    )