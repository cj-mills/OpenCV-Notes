import streamlit as st
import cv2 as cv
import numpy as np

st.title("Image Transformations")

st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")

st.header("Translation")
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translate_horizontal = st.slider(
    "Horizontal Translation",
    min_value=-img_bgr.shape[1],
    max_value=img_bgr.shape[1],
    value=img_bgr.shape[1] // 2,
    step=1,
)
translate_vertical = st.slider(
    "Vertical Translation",
    min_value=-img_bgr.shape[0],
    max_value=img_bgr.shape[0],
    value=img_bgr.shape[0] // 2,
    step=1,
)
translated = translate(img_bgr, translate_horizontal, translate_vertical)
st.image(cv.cvtColor(translated, cv.COLOR_BGR2RGB), caption="Translated")



st.header("Rotation")
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, scale=1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotation_angle = st.slider(
    "Rotation Angle", min_value=0, max_value=360, value=45, step=1,
)
rotated = rotate(img_bgr, rotation_angle)
st.image(cv.cvtColor(rotated, cv.COLOR_BGR2RGB), caption="Rotated")


st.header("Flip")
flip_code = st.radio("Flip Code", (1, 0, -1))
flip = cv.flip(img_bgr, flip_code)
st.image(cv.cvtColor(flip, cv.COLOR_BGR2RGB), caption="Flipped")
