def video_tab():
    import streamlit as st
    import replicate
    import os

    st.header("🎬 AI Video Generator")

    prompt = st.text_input("Enter a prompt for the video you'd like to create:")
    generate = st.button("Generate Video")

    if generate and prompt:
        with st.spinner("Generating video with AnimateDiff..."):
            replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
            replicate.Client(api_token=replicate_token)

            try:
                output = replicate.run(
                    "lucataco/animatediff:main",
                    input={
                        "prompt": prompt,
                        "num_frames": 16,
                        "guidance_scale": 7.5,
                        "width": 512,
                        "height": 512
                    }
                )
                video_url = output.get("video")
                if video_url:
                    st.video(video_url)
                else:
                    st.warning("No video URL returned.")
            except Exception as e:
                st.error(f"Video generation failed: {e}")
