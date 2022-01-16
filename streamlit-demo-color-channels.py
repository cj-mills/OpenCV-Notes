import streamlit as st
import cv2 as cv
import numpy as np

st.title("Color Spaces")

st.header("RGB")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

blank = np.zeros(img_bgr.shape[:2], dtype="uint8")

b, g, r = cv.split(img_bgr)

st.header("Visualize Colors")
blue = cv.merge([b, blank, blank])
st.image(cv.cvtColor(blue, cv.COLOR_BGR2RGB), caption="Visualize Blue")
green = cv.merge([blank, g, blank])
st.image(cv.cvtColor(green, cv.COLOR_BGR2RGB), caption="Visualize Green")
red = cv.merge([blank, blank, r])
st.image(cv.cvtColor(red, cv.COLOR_BGR2RGB), caption="Visualize Red")

st.header("Visualize Color Intensitry")
st.image(b, "Blue Intensity")
st.image(g, "Green Intensity")
st.image(r, "Red Intensity")

st.write(f"Image Shape: {img_bgr.shape}")
st.write(f"Blue Shape: {b.shape}")
st.write(f"Green Shape: {g.shape}")
st.write(f"Red Shape: {r.shape}")

merged = cv.merge([b, g, r])
st.image(cv.cvtColor(merged, cv.COLOR_BGR2RGB), "Merged")
