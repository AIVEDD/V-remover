import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("AIVED PRO")

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file is not None:
    img = Image.open(file)
    st.image(img, caption="Original")
    if st.button("REMOVE BACKGROUND"):
        with st.spinner("Processing..."):
            res = remove(file.getvalue())
            final = Image.open(io.BytesIO(res))
            st.image(final, caption="Result")
            buf = io.BytesIO()
            final.save(buf, format="PNG")
            st.download_button("Download", data=buf.getvalue(), file_name="output.png")
            
