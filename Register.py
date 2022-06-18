import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Prefer Purchase Method?",
    ("PayPal", "Visa Card", "Payoneer", "Wester Union")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose your plan",
        ("Standard", "VIP", "VVIP")
    )

#title
st.title("Join our Student Club!")

#for image
st.image('https://www.schooldata.net/assets/img/suite/applications/student-groups/studentgroups_promo_video.jpg')

 # text input
title = st.text_input('Name')

#choose option
option = st.selectbox(
     'Year',
     ('First year', 'Second year', 'Third year', "Fourth year", "Final year"))

#multiselect
options = st.multiselect(
     'Types of Clubs',
     ['Dance Club', 'Book Club', 'Music Club', 'Swimming Club', "Cultural Club"])

#camera input
picture = st.camera_input("Scan Your Student ID")

#button
st.button('Register')

st.markdown("Thanks for registering :heartpulse:")

