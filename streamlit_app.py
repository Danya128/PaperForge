import streamlit as st

button = False
output = ""

col1, col2 = st.columns(2)

st.markdown("<h1 style='margin-top:-5%;'>PaperForge</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='margin-bottom:5%; margin-top:-2%;'>Your AI study buddy — because deadlines don’t negotiate</h5>", unsafe_allow_html=True)

col1, spacer, col2 = st.columns([4, 1, 6])
with col1:
    st.markdown("<h5 style='margin-top:15%; margin-bottom:5%;'>Please, enter the info about the format of your assignment</h5>", unsafe_allow_html=True)
    description = st.text_input("Title and brief description:")
    no_words = st.text_input("Number of words:")
    ref_style = st.text_input("Referencing style:")
    
    if st.button("Run the process"):
        button = True
        
    if button == True:
        st.markdown("<h6 style='margin-left:70%; margin-top:-20%;'>Loading...</h6>", unsafe_allow_html=True)
        
        
with col2:
    st.markdown("<h5 style='margin-top:10%; margin-bottom:-12%;'>The result:</h5>", unsafe_allow_html=True)
    st.text_area(
        "",
        value=output,
        height=380,
        disabled=True
    )