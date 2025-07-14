def image_gen_tab():
    import streamlit as st
    import replicate
    import os

    st.header("🎨 AI Image Generator")

    prompt = st.text_input("Enter a prompt for the image you'd like to generate:")
    generate = st.button("Generate Image")

    if generate and prompt:
        with st.spinner("Generating image with SDXL..."):
            replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
            replicate.Client(api_token=replicate_token)

            try:
                output = replicate.run(
                    "stability-ai/sdxl:9d50206e9c92d77852ba045c17fd6d83e28d1d62bb82e4cb7c71c7c3f53d0ba6",
                    input={"prompt": prompt}
                )
                st.image(output[0], caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Image generation failed: {e}")
