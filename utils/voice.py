import streamlit as st
import replicate

def voice_tab():
    st.header("🎤 Voice Assistant")

    text = st.text_input("Enter text to convert to voice:")

    if st.button("Generate Voice"):
        if not text:
            st.warning("Please enter some text.")
            return

        try:
            output = replicate.run(
                "suno-ai/bark:db21e45e5e29cd4f7f565c22b9b0487c745cff650ad2b052d3b48fd55b14870a",
                input={"prompt": text}
            )

            audio_url = output
            st.audio(audio_url)

        except Exception as e:
            st.error(f"Voice generation failed: {e}")
