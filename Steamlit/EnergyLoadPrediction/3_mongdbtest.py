import streamlit as st
import database as db
import pandas as pd

st.markdown("test")
df = pd.DataFrame(list(db.fetch_all_periods()))
st.dataframe(df)