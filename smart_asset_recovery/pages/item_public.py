import streamlit as st
from database import cursor

item_id = st.session_state.get("item_id")

cursor.execute(
"SELECT name,photo FROM items WHERE item_id=?",
(item_id,)
)

data = cursor.fetchone()

if data:

    name,photo = data

    st.title("Item Found")

    st.write(name)

    st.image(photo)

    st.success("Location will be sent to owner")

else:

    st.error("Item not found")