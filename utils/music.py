def music_tab():
    import streamlit as st
    import replicate
    import os

    st.header("🎵 Music Generator")

    prompt = st.text_input("Enter a music prompt (e.g. 'lofi chill beat with rain'):")
    generate = st.button("Generate Music")

    if generate and prompt:
        with st.spinner("Composing AI music..."):
            try:
                replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
                replicate.Client(api_token=replicate_token)

                audio_url = replicate.run(
                    "facebookresearch/musicgen:6e2c6021e3ae9cdb005c73d2e87e5a450633f7aa5b0c6f59bfa09d69aa1187ef",
                    input={"prompt": prompt}
                )
                st.success("Here’s your generated music:")
                st.audio(audio_url, format="audio/mp3")
            except Exception as e:
                st.error(f"Music generation failed: {e}")
