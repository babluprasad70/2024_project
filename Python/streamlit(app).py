import streamlit as st
import time as t
import pandas as pd
import numpy as np

# Set page title and icon
st.set_page_config(page_title="Interactive Streamlit Demo", page_icon=":rocket:")

# Import image
st.image("E:\imageforstreamlit.jpg", use_column_width=True)

# Title
st.title("Welcome to My New Project")

# Header
st.header("Machine Learning")

# Subheader
st.subheader("Linear Regression")

# Information
st.info("Information Details of Users")

# Warning message
st.warning("Come early else you will be marked absent")

# Write
st.write("Employee Name")

# Error message
st.error("Wrong message")

# Success message
st.success("Congrats! You have entered the correct password")

# Markdown
st.markdown("# Welcome")
st.markdown("## Welcome")
st.markdown("### Welcome")

# Show emoji and color in text using markdown
st.markdown(":sunglasses:")
st.markdown(":blue-background[i am alone]")

# Caption
st.caption("Write caption here")

# To display mathematical equation
st.latex(r'''a+bx^2+c''')

# Widgets

## Checkbox
st.checkbox("Login")

## Button
st.button("Click")

## Radio widget
st.radio("Pick Your Gender", ["Male", "Female", "Other"])

## Select box
st.selectbox("Pick Your Courses", ["ML", "Cloud", "Cybersecurity"])

## Multiselect
st.multiselect("Choose the Department", ["Content", "Sales", "Marketing"])

## Select slider
st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding"])

## Slider
st.slider("Enter Your Age", 0, 100)

## Number input
st.number_input("Pick Your Number", 0, 100)

## Text input
st.text_input("Enter Your Email ID")

## Date input
st.date_input("Opening Date")

## Time input
st.time_input("Hey, what's the timing?")

## Text area
st.text_area("Welcome here, you can write anything")

## Upload file or folder
st.file_uploader("Upload the files/folder")

## Set color
st.color_picker("Select One Color")

## Checking progress
st.progress(90)

## Spinner
with st.spinner("Just wait..."):
    t.sleep(2)

## Balloon


## Sidebar
st.sidebar.title("Login Here:")
st.sidebar.text_input("Email Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert", ["Students", "Working", "Others"])

# Data Visualization

## Generate random data
data = pd.DataFrame(np.random.randn(50, 2), columns=["X", "Y"])

## Bar chart
st.title("Bar Chart")
st.bar_chart(data)

## Line chart
st.title("Line Chart")
st.line_chart(data)

## Area chart
st.title("Area Chart")
st.area_chart(data)
