import streamlit as st
from data import TIMELINE

st.title(":orange[Education]")

for date, formation, ecole in TIMELINE:
    st.write(f":material/school: **{formation}**")
    st.caption(date)
    st.write(ecole)
    st.divider()