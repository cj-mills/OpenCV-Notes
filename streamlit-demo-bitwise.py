import streamlit as st
import numpy as np
import cv2 as cv


st.title("Bitwise Operators")


blank = np.zeros((400, 400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

st.image(rectangle, "Rectangle")
st.image(circle, "Circle")

# AND Operator
bitwise_and = cv.bitwise_and(rectangle, circle)
st.image(bitwise_and, "AND")

# OR Operator
bitwise_or = cv.bitwise_or(rectangle, circle)
st.image(bitwise_or, "OR")

# XOR Operator
bitwise_xor = cv.bitwise_xor(rectangle, circle)
st.image(bitwise_xor, "XOR")

# NOT Operator
bitwise_not_rect = cv.bitwise_not(rectangle)
st.image(bitwise_not_rect, "NOT Rectangle")

# NOT Operator
bitwise_not_circle = cv.bitwise_not(circle)
st.image(bitwise_not_circle, "NOT Circle")
