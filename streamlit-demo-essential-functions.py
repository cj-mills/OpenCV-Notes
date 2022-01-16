import streamlit as st
import cv2 as cv

st.title("Essential Functions")

st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")


st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")


st.header("Blur")
# Blur
# Image to blur
# Kernel size for the blur filter (larger kernel -> more blur)
# Border pixels are reflected by default
blur_kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, value=9, step=2)
blur = cv.GaussianBlur(img_bgr, (blur_kernel_size, blur_kernel_size), cv.BORDER_DEFAULT)
st.image(cv.cvtColor(blur, cv.COLOR_BGR2RGB), caption="Gaussian Blur")


st.header("Edge Cascade")
threshold_1 = st.slider("Threshold 1", min_value=1, max_value=500, value=125, step=1)
threshold_2 = st.slider("Threshold 2", min_value=1, max_value=500, value=175, step=1)
canny = cv.Canny(img_bgr, threshold_1, threshold_2)
st.image(cv.cvtColor(canny, cv.COLOR_BGR2RGB), caption="Canny Edge Cascade")


st.header("Dilation")
dilate_kernel_size = st.slider(
    "Dilation Kernel Size", min_value=1, max_value=9, value=7, step=2
)
dilate_iterations = st.slider(
    "Dilation Iterations", min_value=1, max_value=10, value=3, step=1
)
dilated = cv.dilate(
    canny, (dilate_kernel_size, dilate_kernel_size), iterations=dilate_iterations
)
st.image(cv.cvtColor(dilated, cv.COLOR_BGR2RGB), caption="Dilated Edges")


st.header("Erotion")
erode_kernel_size = st.slider(
    "Erotion Kernel Size", min_value=1, max_value=9, value=7, step=2
)
erode_iterations = st.slider(
    "Erotion Iterations", min_value=1, max_value=10, value=3, step=1
)
eroded = cv.erode(
    dilated, (erode_kernel_size, erode_kernel_size), iterations=erode_iterations
)
st.image(cv.cvtColor(eroded, cv.COLOR_BGR2RGB), caption="Eroded")


st.header("Resize")
resized_width = st.slider(
    "Resized Width",
    min_value=10,
    max_value=img_bgr.shape[1],
    value=img_bgr.shape[1] // 2,
    step=1,
)
resized_height = st.slider(
    "Resized Height",
    min_value=10,
    max_value=img_bgr.shape[0],
    value=img_bgr.shape[0] // 2,
    step=1,
)
resize = cv.resize(
    img_bgr, (resized_width, resized_height), interpolation=cv.INTER_CUBIC,
)
st.image(cv.cvtColor(resize, cv.COLOR_BGR2RGB), caption="Resized")


st.header("Crop")
col1, col2 = st.columns([1, 1])
width_min = col1.slider(
    "Width Min",
    min_value=10,
    max_value=img_bgr.shape[1],
    value=img_bgr.shape[1] // 4,
    step=1,
)
width_max = col2.slider(
    "Width Max",
    min_value=10,
    max_value=img_bgr.shape[1],
    value=img_bgr.shape[1] // 2,
    step=1,
)

height_min = col1.slider(
    "Height Min",
    min_value=10,
    max_value=img_bgr.shape[0],
    value=img_bgr.shape[0] // 4,
    step=1,
)
height_max = col2.slider(
    "Height Max",
    min_value=10,
    max_value=img_bgr.shape[0],
    value=img_bgr.shape[0] // 2,
    step=1,
)

cropped = img_bgr[height_min:height_max, width_min:width_max]
st.image(cv.cvtColor(cropped, cv.COLOR_BGR2RGB), caption="Cropped")
