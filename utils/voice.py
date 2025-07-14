import streamlit as st
import replicate

def voice_tab():
    st.header("🎤 Voice Assistant")

    text = st.text_input("Enter text to convert to speech")

    if st.button("Generate Voice"):
        if not text:
            st.warning("Please enter some text.")
            return

        try:
            output = replicate.run(
                "m-a-p/musicgen-tts:943df6ac0e4a6671e4b45772d7a3b55a9eb6b0e824d5c85d609eef2f39b6407c",
                input={"text": text}
            )

            audio_url = output["audio"]
            st.audio(audio_url)

        except Exception as e:
            st.error(f"Voice generation failed: {e}")
