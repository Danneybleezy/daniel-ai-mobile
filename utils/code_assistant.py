def code_tab():
    import streamlit as st
    import os
    import requests

    st.header("💻 Code Assistant")

    mode = st.selectbox("What do you want to do?", ["Fix", "Generate", "Explain"])
    user_code = st.text_area("Enter your code or request:")

    run = st.button("Run")

    if run and user_code:
        with st.spinner("Thinking..."):
            try:
                api_key = os.getenv("GROQ_API_KEY", st.secrets.get("GROQ_API_KEY"))
                prompt = f"{mode} this code:\n{user_code}" if mode != "Generate" else user_code

                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "llama3-70b-8192",
                        "messages": [{"role": "user", "content": prompt}]
                    }
                )

                reply = response.json()["choices"][0]["message"]["content"]
                st.code(reply)
            except Exception as e:
                st.error(f"Code Assistant failed: {e}")
