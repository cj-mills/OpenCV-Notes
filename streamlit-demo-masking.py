import streamlit as st
import numpy as np
import cv2 as cv


st.title("Masking")

st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")


blank = np.zeros(img_bgr.shape[:2], dtype="uint8")

rect_col1, rect_col2 = st.columns([1, 1])
rect_col1.subheader("Rectangle Origin")
rect_origin_x = rect_col1.slider(
    "Rect X:", min_value=0, max_value=img_bgr.shape[1], value=30
)
rect_origin_y = rect_col1.slider(
    "Rect Y:", min_value=0, max_value=img_bgr.shape[0], value=30
)

rect_col2.subheader("Rectangle Dimensions")
rect_width = rect_col2.slider(
    "Rect Width:", min_value=0, max_value=img_bgr.shape[1], value=img_bgr.shape[0] // 2
)
rect_height = rect_col2.slider(
    "Rect Height:", min_value=0, max_value=img_bgr.shape[0], value=img_bgr.shape[1] // 2
)
rectangle_mask = cv.rectangle(
    blank.copy(),
    (rect_origin_x, rect_origin_y),
    (rect_origin_x + rect_width, rect_origin_y + rect_height),
    255,
    -1,
)
st.image(cv.cvtColor(rectangle_mask, cv.COLOR_BGR2RGB), "Rectangle Mask")


circle_col1, circle_col2 = st.columns([1, 1])
circle_col1.subheader("Circle Origin")
circle_origin_x = circle_col1.slider(
    "Circle X:", min_value=0, max_value=img_bgr.shape[1], value=img_bgr.shape[1] // 2
)
circle_origin_y = circle_col1.slider(
    "Circle Y:", min_value=0, max_value=img_bgr.shape[0], value=img_bgr.shape[0] // 2
)

circle_col2.subheader("Circle Dimensions")
radius = circle_col2.slider(
    "Radius:", min_value=0, max_value=img_bgr.shape[0], value=100
)
circle_mask = cv.circle(
    blank.copy(), (circle_origin_x, circle_origin_y), radius, 100, -1
)
st.image(cv.cvtColor(circle_mask, cv.COLOR_BGR2RGB), "Circle Mask")

dual_mask = rectangle_mask + circle_mask
st.image(cv.cvtColor(dual_mask, cv.COLOR_BGR2RGB), "Dual Mask")

# AND Operator
bitwise_and = cv.bitwise_and(img_bgr, img_bgr, mask=dual_mask)
st.image(cv.cvtColor(bitwise_and, cv.COLOR_BGR2RGB), "AND")

# OR Operator
bitwise_or = cv.bitwise_or(img_bgr, img_bgr, mask=dual_mask)
st.image(cv.cvtColor(bitwise_or, cv.COLOR_BGR2RGB), "OR")

# XOR Operator
bitwise_xor = cv.bitwise_xor(img_bgr, img_bgr, mask=dual_mask)
st.image(cv.cvtColor(bitwise_xor, cv.COLOR_BGR2RGB), "XOR")

# NOT Operator
bitwise_not = cv.bitwise_not(img_bgr, mask=dual_mask)
st.image(cv.cvtColor(bitwise_not, cv.COLOR_BGR2RGB), "NOT Dual")
