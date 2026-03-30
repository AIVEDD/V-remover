import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Aived | AI Background Remover",
    page_icon="✂️",
    layout="centered"
)

# --- PREMIUM CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: #0E1117;
        color: #FFFFFF;
    }
    /* Main Title Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(#00FFAA, #00CCFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #888;
        font-size: 18px;
        margin-bottom: 40px;
    }
    /* Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #00FFAA 0%, #00CCFF 100%);
        color: #000000;
        font-weight: 700;
        font-size: 16px;
        border: none;
        padding: 15px;
        transition: 0.4s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px rgba(0, 255, 170, 0.4);
        transform: translateY(-2px);
    }
    /* File Uploader Design */
    .stFileUploader {
        border: 2px dashed #333;
        border-radius: 15px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 class='main-title'>AIVED PRO</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Next-Gen AI Powered Background Removal</p>", unsafe_allow_html=True)

# --- CORE FUNCTIONALITY ---
uploaded_file = st.file_uploader("Drop your image here or click to browse", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Displaying Input Image
    input_image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Input Image")
        st.image(input_image, use_container_width=True)
    
    # Process Action
    if st.button('PROCESS IMAGE'):
        with st.spinner('Artificial Intelligence is analyzing your image...'):
            try:
                # Core AI Logic
                input_bytes = uploaded_file.getvalue()
                output_bytes = remove(input_bytes)
                output_image = Image.open(io.BytesIO(output_bytes))
                
                with col2:
                    st.markdown("#### Output Result")
                    st.image(output_image, use_container_width=True)
                    
                    # Prepare Download
                    buf = io.BytesIO()
                    output_image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="📥 DOWNLOAD HD PNG",
                        data=byte_im,
                        file_name="Aived_Result.png",
                        mime="image/png"
                    )
                st.toast("Success! Background removed perfectly.", icon='✅')
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; opacity: 0.5; font-size: 14px;'>"
    "&copy; 2026 AIVED Technologies | Built for Professionals"
    "</p>", 
    unsafe_allow_html=True
                  )
