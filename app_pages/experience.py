import streamlit as st
from data import EXPERIENCES, EXPERIENCES_ASSO

st.title(":orange[Expériences]")

tab_pro, tab_asso = st.tabs([
    ":material/work: Expériences professionnelles",
    ":material/groups: Expériences associatives"
])

with tab_pro:
    for exp in EXPERIENCES:
        st.divider()
        left, right = st.columns([1.5, 2.5])
        with left:
            st.subheader(exp["title"])
            st.caption(exp["company"])
            st.caption(f"{exp['start']} - {exp['end']}")

        with right:
            st.write("")
            st.write("") 
            st.markdown("**Missions & réalisations**")
            st.write(exp["description"])
            st.markdown(" ".join(f":green-badge[{tag}]" for tag in exp["tags"]))
            st.markdown(f"[Voir l'entreprise ↗]({exp['link']})")
with tab_asso:
    for exp in EXPERIENCES_ASSO:
        st.divider()
        left, right = st.columns([1.5, 2.5])

        with left:
            st.subheader(exp["title"])
            st.caption(exp["association"])
            st.caption(f"{exp['start']} — {exp['end']}")

        with right:
            st.write("")
            st.write("")
            st.markdown("**En quelques mots...**")
            st.write(exp["description"])
            st.markdown(
                f"[Découvrir l'association ↗]({exp['link']})"
            )
