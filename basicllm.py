import streamlit as st
from langchain.llms import GooglePalm

# Initialize the PaLM LLM with LangChain

llm = GooglePalm(google_api_key=apikey, temperature=0.2)

# Streamlit app
st.title("Google PaLM Text Generator")
st.write("Enter a prompt to generate text using the Google PaLM API.")

# User input
user_prompt = st.text_input("Enter your prompt:")


# Button to generate text
if st.button("Generate Response"):
    if user_prompt:
        try:
            # Generate response using the LLM
            response = llm(user_prompt)
            st.info(response)
            st.write("**Response from Google PaLM:**")
            st.write(response)
        except TypeError as te:
            st.error("A type error occurred. This is likely due to a keyword argument issue.")
            st.write(f"Error details: {te}")
        except Exception as e:
            st.error("An unexpected error occurred.")
            st.write(f"Error details: {e}")
    else:
        st.warning("Please enter a prompt.")
