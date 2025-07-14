def image_editor_tab():
    import streamlit as st
    import replicate
    import os
    from PIL import Image
    import tempfile

    st.header("🖼️ Image Enhancer")

    uploaded_image = st.file_uploader("Upload an image to enhance", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Original Image", use_column_width=True)

        enhance_btn = st.button("Enhance Image")

        if enhance_btn:
            with st.spinner("Enhancing with Real-ESRGAN..."):
                replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
                replicate.Client(api_token=replicate_token)

                # Save to temp file
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                    image.save(tmp.name)
                    model_input = open(tmp.name, "rb")

                    output_url = replicate.run(
                        "sczhou/codeformer:1e1ff7b031cb93c4ad0f86962f1a1a261dd3dcd55509e8a494c1312eab8caa56",
                        input={"image": model_input, "codeformer_fidelity": 0.7}
                    )

                st.success("Enhanced Image:")
                st.image(output_url, use_column_width=True)
