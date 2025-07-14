def pdf_tab():
    import streamlit as st
    import PyPDF2
    import os
    import requests

    st.header("📄 PDF Summarizer")

    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

    if uploaded_file:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.subheader("Document Preview:")
        st.text_area("Extracted Text", text[:1000] + "...", height=200)

        if st.button("Summarize Document"):
            with st.spinner("Summarizing using Groq..."):
                try:
                    api_key = os.getenv("GROQ_API_KEY", st.secrets.get("GROQ_API_KEY"))
                    response = requests.post(
                        "https://api.groq.com/openai/v1/chat/completions",
                        headers={
                            "Authorization": f"Bearer {api_key}",
                            "Content-Type": "application/json"
                        },
                        json={
                            "model": "llama3-70b-8192",
                            "messages": [{"role": "user", "content": f"Summarize this:\n{text[:4000]}"}]
                        }
                    )
                    reply = response.json()["choices"][0]["message"]["content"]
                    st.success("Summary:")
                    st.write(reply)
                except Exception as e:
                    st.error(f"Summarization failed: {e}")
