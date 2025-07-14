def avatar_tab():
    import streamlit as st
    import replicate
    import os
    from PIL import Image
    import tempfile

    st.header("🧑‍🎨 AI Avatar Creator")

    uploaded_image = st.file_uploader("Upload a selfie or face image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="Original Image", use_column_width=True)

        if st.button("Create Animated Avatar"):
            with st.spinner("Generating animated avatar..."):
                try:
                    replicate_token = os.getenv("REPLICATE_API_TOKEN", st.secrets.get("REPLICATE_API_TOKEN"))
                    replicate.Client(api_token=replicate_token)

                    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
                        img = Image.open(uploaded_image).convert("RGB")
                        img.save(tmp.name)
                        file_data = open(tmp.name, "rb")

                        output = replicate.run(
                            "cjwbw/animate-face:99bfc50284eb180620c9e5d2c8e9f29b9baf4d9cf61d9f50249a7be47c2e0ec4",
                            input={"image": file_data}
                        )

                        if isinstance(output, str):
                            st.video(output)
                        else:
                            st.warning("Avatar generation may have failed.")
                except Exception as e:
                    st.error(f"Avatar creation failed: {e}")
