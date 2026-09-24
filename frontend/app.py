import streamlit as st
import requests

st.set_page_config(page_title="LegalEase", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    
    st.image("Image/logo.png", use_container_width=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

document_type = st.text_input("Document Type")
parties = st.text_area("Parties Involved") 
terms = st.text_area("Terms and Conditions")
dates = st.text_input("Effective Dates")
    

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""    

if st.button("Generate Document"):
    with st.spinner("Drafting your legal document..."):                
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }
                
        try:
            response = requests.post("http://localhost:8000/generate", json=payload)
                
            if response.status_code == 200:                    
                
                st.session_state.generated_text = response.json().get("document", "")
                st.success("Document Generated Successfully!")
            else:
                st.error(f"Backend Error: {response.status_code}")
                    
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to backend. Is FastAPI running?")


if st.session_state.generated_text:
    edited_text = st.text_area("Edit Document Below:", st.session_state.generated_text, height=300)
        
    st.download_button(
        label="Download as .TXT",
        data=edited_text,
        file_name="legal_document.txt",
        mime="text/plain"
    )