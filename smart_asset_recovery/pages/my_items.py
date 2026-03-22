import streamlit as st
import pandas as pd
from database import conn

st.title("My Items")

email = st.session_state.user

query = "SELECT * FROM items WHERE owner_email=?"

df = pd.read_sql(query, conn, params=(email,))

st.dataframe(df)