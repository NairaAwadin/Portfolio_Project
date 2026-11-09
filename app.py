import streamlit as st
from data import PROFILE

st.set_page_config(
    page_title=PROFILE["name"],
    page_icon="briefcase",
    layout="wide",
    )

with st.sidebar:
    #st.image("assets/photo.png", width=120)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"[LinkedIn]({PROFILE['linkedin']})")
    st.markdown(f"[GitHub]({PROFILE['github']})")

pages = [
    st.Page("pages/home.py", title="A propos", icon=":material/person:"),
    st.Page("pages/projects.py", title="Mes Projets", icon=":material/code:"),
    st.Page("pages/skills.py", title="Compétences", icon=":material/bar_chart:"),
    st.Page("pages/education.py", title="Education", icon=":material/school:"),
    st.Page("pages/contact.py", title="Contacte", icon=":material/mail:")
]

st.navigation(pages).run()
