import streamlit as st
import pandas as pd
from data import SKILLS, SOFT_SKILLS, TOOLS, PROJECTS

st.title(":orange[Compétences]")

left, right = st.columns(2)
skills = list(SKILLS.items())

with left:
    st.subheader("Compétences techniques")
    for skill, level in skills[:len(skills)//2]:
        st.progress(level / 100, text=f"{skill} : {level}%")

with right:
    st.subheader(" ")
    for skill, level in skills[len(skills)//2:]:
        st.progress(level / 100, text=f"{skill} : {level}%")

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("Outils")
    tools_list = " ".join(f":green-badge[{tool}]" for tool in TOOLS)
    st.markdown(tools_list)

with right:
    st.subheader("Compétences transversales")
    soft_list = " ".join(f":orange-badge[{skill}]" for skill in SOFT_SKILLS)
    st.markdown(soft_list)

st.divider()

df = pd.DataFrame(PROJECTS)
df = df.explode("tags")
df = df["tags"].value_counts()
st.subheader("Répartition des compétences dans mes projets")
st.bar_chart(df, color="#F2C14E")
