def voice_tab():
    import streamlit as st
    import os
    import requests

    st.header("🎤 Voice Assistant")

    st.markdown("This assistant can **read responses aloud**. Voice input coming soon.")

    text_input = st.text_area("Type what you'd like me to say aloud:")
    speak_button = st.button("🔊 Speak")

    if speak_button and text_input:
        with st.spinner("Generating voice..."):
            try:
                # Using ElevenLabs-like text-to-speech via replicate
                replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
                import replicate
                replicate.Client(api_token=replicate_token)

                audio_url = replicate.run(
                    "cjwbw/xtts-v2:2a50dcd3f3f798d7c80e0a8a63b98355f8a9c6bb9fce65c2c066d1264c4b1549",
                    input={
                        "text": text_input,
                        "speaker": "default"
                    }
                )
                if isinstance(audio_url, str):
                    st.audio(audio_url, format="audio/wav")
                else:
                    st.warning("No audio generated.")
            except Exception as e:
                st.error(f"Voice generation failed: {e}")
