import streamlit as sl
from PIL import Image
sl.set_page_config(
    page_title="Image Resizer",
    page_icon="img.png"
)
sl.markdown("<h1><center>Image Resizer</center></h1>", unsafe_allow_html=True)
original_img = sl.file_uploader("Upload Image", type=("jpg", "jpeg", "png"))
if original_img:
    img = Image.open(original_img)
    height = img.height
    width = img.width
    sl.markdown("<h3>Image Information</h3>", unsafe_allow_html=True)
    sl.markdown(f"Height: {height}", unsafe_allow_html=True)
    sl.markdown(f"Width: {width}", unsafe_allow_html=True)
    sl.markdown(f"Formate: {img.format}", unsafe_allow_html=True)
    sl.markdown("<h3>Resizing</h3>", unsafe_allow_html=True)
    col1, col2 = sl.columns(2, gap="medium")
    h = col1.number_input("Height", value=height)
    w = col2.number_input("Weight", value=width)
    r = col1.number_input("Rotation", value=0, step=90, max_value=360, min_value=0)
    formate = col2.selectbox("Formate", ("JPEG", "PNG", "GIF"))
    button = sl.button("Submit")
    if button:
        edited = img.resize((w, h)).rotate(r)
        sl.image(edited)
        

