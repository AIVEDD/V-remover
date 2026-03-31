import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("AIVED PRO - BG Remover")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='Selected Image')
    
    if st.button('Remove Background'):
        with st.spinner('AI is working...'):
            output = remove(uploaded_file.getvalue())
            res_img = Image.open(io.BytesIO(output))
            st.image(res_img, caption='Final Result')
            
            buf = io.BytesIO()
            res_img.save(buf, format="PNG")
            st.download_button("Download PNG", data=buf.getvalue(), file_name="aived.png")
            
                  )
