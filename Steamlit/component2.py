import streamlit as st

# Text/title
st.title("This is a header")

# Header/Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello streamlit")

# Markdown
st.markdown("### This is a Markdown")

# Error/Colorful text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error Danger")
st.exception("NameError('name three not defined')")

# Get Help info about python
st.help(range)

# Writing text/Super Fxn
st.write("Text with write")
st.write(range(10))

# Image
from PIL import Image
img = Image.open("beijing.jpg")
st.image(img, width=300, caption="Beijing")

# Videos
vid_file = open("nanjing.mp4", "rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

# Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status?",("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
else:
    st.warning("You are inactive")

# SelectBox
occupation = st.selectbox("You occupation", ["Programmer", "DataScientist", "Doctor", "Businessman"])
st.write("You select this option ", occupation)

# MultiSelect
location = st.multiselect("Where do you work?", ("London", "New york", "Hongkong", "Tokyo"))
st.write("you selected ", len(location), "location")

# Slider
level = st.slider("What is your level?", 1, 5)
st.write("Your level is ", level)

# Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is cool")

# Text Input
firstName = st.text_input("Enter your firstname", "Type here...")
if st.button("Submit", key=1):
    result = firstName.title()
    st.success(result)

# Text Area
message = st.text_area("Enter your message", "Type here...")
if st.button("Submit", key=2):
    result = message.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time = st.time_input("The time is ", datetime.time())

# Display JSON
st.text("Display JSON")
st.json({'name': "Zongyang", 'age': 18})

# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code
with st.echo():
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(100):
    my_bar.progress(p +1)
    time.sleep(0.01)
st.success("Finished")

# Balloons
# st.balloons()

# SideBars
st.sidebar.header("About")
st.sidebar.text("This is streamlit")

# Function
@st.cache
def run_fxn():
    print("foo")
    return range(100)
st.write(run_fxn())

