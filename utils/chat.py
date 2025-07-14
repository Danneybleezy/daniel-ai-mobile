def chat_tab():
    import streamlit as st
    import requests
    import os

    st.header("💬 Daniel😎 Chat")

    model = st.selectbox("Choose model", ["Groq (LLaMA 3)", "Gemini (Pro or Flash)"])
    user_input = st.text_area("You:", "", height=100)
    submitted = st.button("Send")

    if submitted and user_input:
        if model.startswith("Groq"):
            api_key = os.getenv("GROQ_API_KEY", st.secrets.get("GROQ_API_KEY"))
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            body = {
                "model": "llama3-70b-8192",
                "messages": [{"role": "user", "content": user_input}]
            }
            response = requests.post(url, headers=headers, json=body)
            try:
                reply = response.json()['choices'][0]['message']['content']
                st.markdown(f"**Daniel😎:** {reply}")
            except:
                st.error("Failed to get response from Groq API.")
        else:
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GEMINI_API_KEY", st.secrets.get("GEMINI_API_KEY")))
            gemini = genai.GenerativeModel("gemini-pro")
            try:
                response = gemini.generate_content(user_input)
                st.markdown(f"**Daniel😎:** {response.text}")
            except Exception as e:
                st.error(f"Gemini error: {e}")
