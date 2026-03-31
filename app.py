import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="AIVED PRO", layout="centered")

st.title("✂️ AIVED PRO")
st.write("Professional Background Remover")

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file is not None:
    img = Image.open(file)
    st.image(img, caption="Original Image")
    
    if st.button("REMOVE BACKGROUND"):
        with st.spinner("AI is processing..."):
            input_data = file.getvalue()
            output_data = remove(input_data)
            final_img = Image.open(io.BytesIO(output_data))
            
            st.image(final_img, caption="Background Removed")
            
            buf = io.BytesIO()
            final_img.save(buf, format="PNG")
            st.download_button("📥 Download Result", data=buf.getvalue(), file_name="aived_result.png")
            
