import streamlit as st
from langchain.llms import GooglePalm

# Initialize the PaLM LLM with LangChain
apikey = "AIzaSyCWGkTI119Jf4T8fnbWi9DRGrwD4jpEBn4"
llm = GooglePalm(google_api_key=apikey, temperature=0.2)

# Streamlit app
st.title("Google PaLM Text Generator")
st.write("Generate text using a fixed prompt with the Google PaLM API.")

# Fixed prompt
fixed_prompt = "Tell me about the benefits of using AI in healthcare."

# Display the fixed prompt
st.write(f"**Prompt:** {fixed_prompt}")

# Button to generate text
if st.button("Generate Response"):
    # Generate response using the LLM
    response = llm(fixed_prompt)
    st.write("**Response from Google PaLM:**")
    st.write(response)
