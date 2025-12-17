import streamlit as st

st.title("Machine Learning project")
from PIL import Image
img = Image.open("1.jpg")
# st.image(img)
st.image(img, width=300, caption="sample image")

# adding video to our streamlit application

# adding audio to our streamlit application
audio = open("pop.mp3", "rb")
audio_file = audio.read()
st.audio(audio_file)

# checkbox
if st.checkbox("Show/hide"):
    st.text("Showing/Hiding widget")

# radio-buttons
status = st.radio("What is your status", ("Active", "Inactive"))

# link with some function
if status == "Active":
    st.success("You are an active member")
else:
    st.warning("You are an inactive member")

# select box
occupation = st.selectbox("Your occupation", ["Programmer", "Doctor", "AI Engineer", "Businessman"])
st.write(f"You selected the occupation {occupation}")

# slider
level = st.slider("What is your level", 1,5)

# buttons
st.button("Simple button", key=2)
if st.button("About", key=1):
    st.text("Streamlit is cool")

# text input
first_name = st.text_input("Enter your first name")
if st.button("Submit", key=3):
    result = "first name submitted successfully"
    st.success(result)

# text area
message = st.text_area("Enter your message", "Type here...")
if st.button("Submit", key=4):
    result = message.title()
    st.success(result)

# date and time
import datetime
today = st.date_input("Today is", datetime.datetime.now)