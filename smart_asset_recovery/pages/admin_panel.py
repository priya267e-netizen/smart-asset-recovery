import streamlit as st
import pandas as pd
from database import conn

st.title("Admin Panel")

users = pd.read_sql("SELECT * FROM users",conn)

items = pd.read_sql("SELECT * FROM items",conn)

st.subheader("Users")

st.dataframe(users)

st.subheader("Items")

st.dataframe(items)