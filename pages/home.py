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

st.divider()
col1, col2, col3 = st.columns(3)

col1.metric("Projects", len(PROJECTS))
col2.metric("Skills", len(SKILLS))

best_skill = None
niv_max = 0

# pour trouver la compétence avec le niv le plus élévé
for skill, niv in SKILLS.items():
    if niv > niv_max:
        niv_max = niv
        best_skill = skill

col3.metric("Compétence principale", best_skill)

