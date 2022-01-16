import streamlit as st
import cv2 as cv

st.title("Drawing Shapes and Text")
st.header("Input Image")
img_bgr = cv.imread("images/flower.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")


st.header("Shape Selection")
shape_option = st.selectbox(
    "Select a shape", ("Rectangle", "Circle", "Line", "Text"), index=0
)

st.subheader("Shape Color")
color_picker_col1, color_picker_col2 = st.columns([1, 1])
shape_color = color_picker_col1.color_picker("Pick A Color", "#00f900")
color_picker_col2.write(f"Hex Color Code: {shape_color}")
color_r = int(shape_color[1:3], 16)
color_g = int(shape_color[3:5], 16)
color_b = int(shape_color[5:7], 16)
color_picker_col2.write(f"RGB Color Code: ({color_r},{color_g},{color_b})")


col1, col2 = st.columns([1, 1])
col1.subheader("Origin Coorindates")
origin_x = col1.number_input("X:", min_value=0, max_value=img_bgr.shape[1], value=20)
origin_y = col1.number_input("Y:", min_value=0, max_value=img_bgr.shape[0], value=20)

if shape_option == "Rectangle":
    col2.subheader("Dimensions")
    width = col2.number_input(
        "Width:", min_value=0, max_value=img_bgr.shape[1], value=40
    )
    height = col2.number_input(
        "Height:", min_value=0, max_value=img_bgr.shape[0], value=40
    )
    thickness = st.slider("Thickness", min_value=-1, max_value=20, value=2)
    cv.rectangle(
        # Image to draw on
        img_bgr,
        # Starting coords
        (origin_x, origin_y),
        # ending coords
        (origin_x + width, origin_y + height),
        # Color (in BGR)
        (color_b, color_g, color_r),
        # Line thickness (-1 to fill the shape)
        thickness=thickness,
    )
if shape_option == "Circle":
    col2.subheader("Dimensions")
    radius = col2.number_input(
        "Radius:", min_value=0, max_value=(min(img_bgr.shape[:2]) // 2), value=40
    )
    thickness = st.slider("Thickness", min_value=-1, max_value=20, value=2)
    cv.circle(
        # Image to draw on
        img_bgr,
        # Starting coords
        (origin_x, origin_y),
        # Radius
        radius,
        # Color (in BGR)
        (color_b, color_g, color_r),
        # Line thickness (-1 to fill the shape)
        thickness=thickness,
    )
if shape_option == "Line":
    col2.subheader("Ending Coordinates")
    end_x = col2.number_input("X:", min_value=0, max_value=img_bgr.shape[1], value=40)
    end_y = col2.number_input("Y:", min_value=0, max_value=img_bgr.shape[0], value=40)
    thickness = st.slider("Thickness", min_value=1, max_value=40, value=2)
    cv.line(
        # Image to draw on
        img_bgr,
        # Starting coords
        (origin_x, origin_y),
        # Ending coords
        (end_x, end_y),
        # Color (in BGR)
        (color_b, color_g, color_r),
        # Line thickness
        thickness=thickness,
    )
if shape_option == "Text":
    col2.subheader("Input")
    text = col2.text_input("Enter some text:", "Hello World")
    font_size = col2.number_input(
        "Font Size:", min_value=0.0, max_value=10.0, value=1.0
    )
    cv.putText(
        # Image to draw on
        img_bgr,
        # Text
        text,
        # Starting coords
        (origin_x, origin_y),
        # Font type
        cv.FONT_HERSHEY_TRIPLEX,
        # Font size
        font_size,
        # Color (in BGR)
        (color_b, color_g, color_r),
    )
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Output")

