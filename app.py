import streamlit as st
from data import PROFILE

st.set_page_config(
    page_title=PROFILE["name"],
    page_icon=":briefcase",
    layout="wide",
    )

with st.sidebar:
    st.image("assets/photo.png", width=110)
    st.markdown(f"### {PROFILE['name']}")
    st.caption(PROFILE["title"])
    st.markdown(f":material/work: [LinkedIn]({PROFILE['linkedin']})")
    st.markdown(f":material/code: [GitHub]({PROFILE['github']})")

    st.divider()

    if "visits" not in st.session_state:
        st.session_state["visits"] = 0
    st.session_state["visits"] += 1
    st.caption(f"T'as interagis {st.session_state['visits']} fois avec le site !")

app_pages = [
    st.Page("app_pages/home.py", title="A propos", icon=":material/person:"),
    st.Page("app_pages/projects.py", title="Mes Projets", icon=":material/code:"),
    st.Page("app_pages/experience.py", title="Expériences", icon=":material/work:"),
    st.Page("app_pages/skills.py", title="Compétences", icon=":material/bar_chart:"),
    st.Page("app_pages/education.py", title="Education", icon=":material/school:"),
    st.Page("app_pages/contact.py", title="Contact", icon=":material/mail:")
]

st.navigation(app_pages).run()
