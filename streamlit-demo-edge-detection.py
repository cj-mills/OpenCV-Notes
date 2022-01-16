import streamlit as st
import numpy as np
import cv2 as cv


st.title("Edge Detection")

st.header("Input Image")
img_bgr = cv.imread("images/flower_2.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")

st.header("Laplacian")
lap = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
st.image(lap, "Laplacian")

st.header("Sobel")
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)

st.image(sobelx, "Sobel X", clamp=True)
st.image(sobely, "Sobel Y", clamp=True)
st.image(cv.bitwise_or(sobelx, sobely), "Sobel Combined")

st.header("Canny")
threshold_1 = st.slider("Threshold 1", min_value=1, max_value=500, value=125, step=1)
threshold_2 = st.slider("Threshold 2", min_value=1, max_value=500, value=175, step=1)
canny = cv.Canny(img_bgr, threshold_1, threshold_2)
st.image(cv.cvtColor(canny, cv.COLOR_BGR2RGB), caption="Canny")
