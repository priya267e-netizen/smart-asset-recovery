import streamlit as st
from auth import login_user

st.title("Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):

    if login_user(email, password):

        # Login session create
        st.session_state.logged_in = True
        
        # Email மட்டும் store
        st.session_state.user = email

        st.success("Login successful")

        st.rerun()

    else:

        st.error("Invalid email or password")