import streamlit as st
import requests
import os
# Vext API configuration
VEXT_API_URL = "https://payload.vextapp.com/hook/239WJBPHQJ/catch/hello" 
API_KEY = os.environ.get('FINANCE_TEACHER_VEXT_API_KEY') 

if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set")

st.set_page_config(page_title="Vext-Powered App", page_icon="🤖", layout="wide")

st.title("🤖 myFinanceTeacher Vext-Powered App")

st.markdown("""
This app uses the Vext API to process your text. Simply enter your text in the box below and click 'Process' to see the results.
""")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("Enter your text here:", height=200)
    process_button = st.button("Process", key="process")

with col2:
    st.subheader("Results")
    result_placeholder = st.empty()

if process_button:
    if user_input:
        with st.spinner("Processing..."):
            # Call Vext API
            headers = {
            #    "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "Apikey" : f"Api-key {API_KEY}",
            }
            data = {"payload": user_input}
            
            try:
                response = requests.post(VEXT_API_URL, json=data, headers=headers)
                response.raise_for_status()
                
                result = response.json()
                result_placeholder.success("Processing complete!")
                result_placeholder.write(result['text'])
             #   result_placeholder.json(result)
            except requests.exceptions.RequestException as e:
                result_placeholder.error(f"Error: {str(e)}")
    else:
        result_placeholder.warning("Please enter some text to process.")

st.markdown("---")
st.markdown("Powered by Vext AI")
