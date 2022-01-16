import streamlit as st
import cv2 as cv

st.title("Blur")

st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

st.header("Average Blur")
avg_kernel_size = st.slider(
    "Average Kernel Size", min_value=1, max_value=15, value=7, step=2
)
average = cv.blur(img_bgr, (avg_kernel_size, avg_kernel_size))
st.image(cv.cvtColor(average, cv.COLOR_BGR2RGB), "Average Blur")

st.header("Gaussian Blur")
# Gives weight to each pixel in the kernal window
# Basically a weighted average blur?
gaussian_kernel_size = st.slider(
    "Gaussian Kernel Size", min_value=1, max_value=15, value=7, step=2
)
gaussian = cv.GaussianBlur(
    img_bgr, (gaussian_kernel_size, gaussian_kernel_size), sigmaX=0
)
st.image(cv.cvtColor(gaussian, cv.COLOR_BGR2RGB), "Gaussian Blur")

st.header("Median Blur")
# tends to be more effective for reducing noise
# not meant for high kernel sizes
median_kernel_size = st.slider(
    "Median Kernel Size", min_value=1, max_value=35, value=7, step=2
)
median = cv.medianBlur(img_bgr, median_kernel_size)
st.image(cv.cvtColor(median, cv.COLOR_BGR2RGB), "Median Blur")

st.header("Bilateral Blur")
# most effective
bilateral_diameter = st.slider(
    "Bilateral Diameter", min_value=1, max_value=30, value=10, step=1
)
bilateral_sigma_color = st.slider(
    "Bilateral Sigma Color", min_value=1, max_value=100, value=35, step=1
)
bilateral_sigma_space = st.slider(
    "Bilateral Sigma Space", min_value=1, max_value=100, value=25, step=1
)
bilateral = cv.bilateralFilter(
    img_bgr,
    bilateral_diameter,
    sigmaColor=bilateral_sigma_color,
    sigmaSpace=bilateral_sigma_space,
)
st.image(cv.cvtColor(bilateral, cv.COLOR_BGR2RGB), "Bilateral Blur")
