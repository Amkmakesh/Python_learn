import streamlit as MK
from PIL import Image

MK.title("Grayscale convertor")

with MK.expander("camera")


cam_image = MK.camera_input ("camera")

if cam_image:

    img = Image.open(cam_image)

    gray_img = img.convert("L")

    MK.image(gray_img)
