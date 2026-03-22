import streamlit as st

st.title("Dashboard")

menu = st.selectbox(
"Menu",
["Add Item","My Items"]
)

if menu == "Add Item":

    import pages.add_item

if menu == "My Items":

    import pages.my_items