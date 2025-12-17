import streamlit as st

# title
st.title("Machine Learning project")

# header/subheader
st.header("This is a header")
st.subheader("This is a subheader")

# text
st.text("Hello Streamlit")

# markdown
st.markdown("This is our first markdown")
st.markdown("# This is our first markdown") # will act like a title by adding hash

# error/colourful text
st.success("Successfully done")

# information
st.info("Information")

# warning
st.warning("This is a warning")

# error
st.error("This is an error")

# exception
st.exception("This is an exception")

import pandas
st.help(pandas) # tells us the meaning of pandas
import numpy
st.help(numpy)

# writing text super function
st.write("Text with write")
st.write(range(0,10))

# adding the image
from PIL import Image
img = Image.open("1.jpg")
st.image(image=img)

