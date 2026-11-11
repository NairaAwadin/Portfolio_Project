import streamlit as st
from data import PROJECTS
from utils import all_tags, filter_projects, get_year

st.title(":orange[Mes Projets]")

all_tags_p = all_tags(PROJECTS)
selected_tags = st.multiselect("Filtrer par tag", all_tags_p)

filtred_projects = filter_projects(PROJECTS, selected_tags)

tri_annee = st.selectbox("Trier par année", ["Plus récents d'abord", "Plus anciens d'abord"])
if tri_annee == "Plus récents d'abord":
    filtred_projects = sorted(filtred_projects, key=get_year, reverse=True)
else:
    filtred_projects = sorted(filtred_projects, key=get_year)

st.markdown("""
<style>
.desc {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: max-height 0.4s ease, opacity 0.4s ease;
}
div[class*="st-key-card_"]:hover .desc {
    max-height: 300px;
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)

projects_cols = st.columns(3)
for i in range(len(filtred_projects)):
    project = filtred_projects[i]
    col = projects_cols[i % 3]
    card = col.container(border=True, key=f"card_{i}")
    card.image(project["image"])
    card.subheader(project["title"])
    card.markdown(" ".join(f":green-badge[{tag}]" for tag in project["tags"]))
    card.markdown(f'<div class="desc">{project["description"]}</div>', unsafe_allow_html=True)
    card.caption(project["year"])
    card.link_button("Voir GitHub", project["link"])
