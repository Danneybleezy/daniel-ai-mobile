import streamlit as st
import replicate
import tempfile
import base64

def voice_tab():
    st.header("🎤 Voice Assistant")

    user_input = st.text_area("Enter something to speak")

    if st.button("Generate Voice"):
        if user_input.strip() == "":
            st.warning("Please type something.")
            return

        try:
            output = replicate.run(
                "cjwbw/xtts-api:db21e45e5e29cd4f7f565c22b9b0487c745cff650ad2b052d3b48fd55b14870a",
                input={
                    "text": user_input,
                    "language": "en",
                    "speaker": "random"
                }
            )

            audio_url = output["audio"]
            st.audio(audio_url)

        except Exception as e:
            st.error(f"Voice generation failed: {e}")
