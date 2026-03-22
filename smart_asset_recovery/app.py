import streamlit as st
from database import create_tables

create_tables()

query = st.query_params

# QR scan case
if "item" in query:

    st.session_state.item_id = query["item"]

    import pages.item_public

else:

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:

        menu = st.sidebar.selectbox(
        "Menu",
        ["Login","Register"]
        )

        if menu == "Login":
            import pages.login

        if menu == "Register":
            import pages.register

    else:

        import pages.dashboard