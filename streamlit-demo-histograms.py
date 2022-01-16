import streamlit as st
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


st.title("Computing Histograms")

st.header("Input Image")
img_bgr = cv.imread("images/flower_2.jpg")
st.image(cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB), caption="Input")


st.header("Grayscale")
gray = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
st.image(gray, caption="Grayscale")

gray_hist = cv.calcHist(
    [gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256]
)

fig, ax = plt.subplots()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
ax.hist(gray_hist, bins=20)
st.pyplot(fig)


st.header("Color")
colors = ("b", "g", "r")

fig, ax = plt.subplots()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim([0, 256])
for i, col in enumerate(colors):
    hist = cv.calcHist(
        [img_bgr], channels=[i], mask=None, histSize=[256], ranges=[0, 256]
    )
    plt.plot(hist, color=col)
st.pyplot(fig)
