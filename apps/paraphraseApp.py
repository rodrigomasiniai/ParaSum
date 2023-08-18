import streamlit as st
from paraphraser import text_paraphrase


st.title('Paraphraser')
st.write('Please provide the text to be paraphrased')
user_input = st.text_area('Enter text','')
if user_input:        
    output = text_paraphrase(user_input)
    st.write("Paraphrased Text: ")
    st.write(output)
