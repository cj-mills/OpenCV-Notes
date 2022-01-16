import streamlit as st
import cv2 as cv
import numpy as np

st.title("Color Spaces")

st.header("RGB")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

st.header("BGR")
st.image(img_bgr, "BGR")

st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")

st.header("BGR to HSV (Hue Saturation and Value)")
hsv = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
st.image(hsv, "HSV")

st.header("BGR to LAB")
lab = cv.cvtColor(img_bgr, cv.COLOR_BGR2LAB)
st.image(lab, "LAB")

st.header("Grayscale to HSV")
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
bgr_hsv = cv.cvtColor(gray_bgr, cv.COLOR_BGR2HSV)
st.image(bgr_hsv, "Gray to HSV")
