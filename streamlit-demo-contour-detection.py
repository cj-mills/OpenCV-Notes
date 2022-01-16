import streamlit as st
import cv2 as cv
import numpy as np

st.title("Contour Detection")

st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

blank = np.zeros(img_bgr.shape, dtype="uint8")

st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")


st.header("Edge Cascade")
threshold_1 = st.slider("Threshold 1", min_value=1, max_value=500, value=125, step=1)
threshold_2 = st.slider("Threshold 2", min_value=1, max_value=500, value=175, step=1)
canny = cv.Canny(img_bgr, threshold_1, threshold_2)
st.image(cv.cvtColor(canny, cv.COLOR_BGR2RGB), caption="Canny Edge Cascade")


st.header("Find Contours")
# Find Countours
# Looks at the edges found in an image
# Returns a list of coordinates for all contours found in an image
# and a hierarchical representation of the contours
# CHAIN_APPROX_NONE: does nothing
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
st.write(f"Found {len(contours)} contours")

st.header("Threshold")
# Pixels with intensity below 125 are set to black
# Pixels with intensity above 125 are set to white
threshold = st.slider("Threshold", min_value=0, max_value=255, value=125, step=1)
ret, thresh = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)
st.image(cv.cvtColor(thresh, cv.COLOR_BGR2RGB), caption="Threshold")

st.header("Find Contours #2")
# Looks at the edges found in an image
# Returns a list of coordinates for all contours found in an image
# and a hierarchical representation of the contours
# CHAIN_APPROX_NONE: does nothing
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
st.write(f"Found {len(contours)} contours")

st.header("Visualize contours")
cv.drawContours(blank, contours, -1, (0, 0, 255), thickness=1)
st.image(cv.cvtColor(blank, cv.COLOR_BGR2RGB), caption="Contours")
