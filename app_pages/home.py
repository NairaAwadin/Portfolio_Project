import streamlit as st
from data import PROFILE, PROJECTS, SKILLS

left, right = st.columns([2, 1])

with left:
    st.title(f"Salut, moi c'est {PROFILE['name']}")
    st.divider()
    st.subheader(PROFILE["title"])
    st.write(PROFILE["about"])
    st.markdown(f":material/mail: {PROFILE['email']}")
    
    st.markdown(
        f":material/code: [GitHub]({PROFILE['github']})"
        f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        f":material/work: [LinkedIn]({PROFILE['linkedin']})"
    ) 

    with open("assets/Naira_AWADIN_CV_Resume.pdf", "rb") as f:
        st.download_button("Télécharger mon CV", f, file_name="Naira_Awadin_CV.pdf", icon=":material/download:")

with right:
    st.write("")
    st.write("")
    st.image("assets/photo.png", width=220)

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Projets", len(PROJECTS))
col2.metric("Compétences", len(SKILLS))

best_skill = None
niv_max = 0

for skill, niv in SKILLS.items():
    if niv > niv_max:
        niv_max = niv
        best_skill = skill

col3.metric("Point fort", best_skill)
