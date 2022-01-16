import streamlit as st
import numpy as np
import cv2 as cv


st.title("Thresholding Images")

st.header("Input Image")
img_bgr = cv.imread("images/flower_2.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

st.header("Simple Thresholding")
simple_thresh = st.slider(
    "Simple Threshold", min_value=0, max_value=255, value=100, step=1
)
threshold, thresh = cv.threshold(
    img_bgr, thresh=simple_thresh, maxval=255, type=cv.THRESH_BINARY
)
st.image(cv.cvtColor(thresh, cv.COLOR_BGR2RGB), "Simple Threshold")

st.header("Inverse Thresholding")
inv_thresh = st.slider(
    "Inverse Threshold", min_value=0, max_value=255, value=100, step=1
)
threshold, thresh_inv = cv.threshold(
    img_bgr, thresh=inv_thresh, maxval=255, type=cv.THRESH_BINARY_INV
)
st.image(cv.cvtColor(thresh_inv, cv.COLOR_BGR2RGB), "Threshold Inverse")


st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")

st.header("Adaptive Threshold")
blocksize = st.slider("Blocksize", min_value=3, max_value=33, value=11, step=2)
adaptive_thresh = cv.adaptiveThreshold(
    gray,
    maxValue=255,
    adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
    thresholdType=cv.THRESH_BINARY,
    blockSize=blocksize,
    C=3,
)
st.image(adaptive_thresh, "Adaptive Thresholding")
