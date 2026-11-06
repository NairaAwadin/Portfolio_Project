import streamlit as st
from data import PROFILE, PROJECTS, SKILLS

st.title(f"Salut, moi c'est {PROFILE['name']}")
st.subheader(PROFILE["title"])

left, right = st.columns([1, 2])
#with left:
    #st.image("assets/photo.png", width=220)

with right:
    st.write(PROFILE["about"])
    st.write(PROFILE["email"])
    with open("assets/cv_naira.pdf", "rb") as f:
        st.download_button("Télécharger CV", f, file_name="cv_naira.pdf")
