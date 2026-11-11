import streamlit as st
from utils import check_informations, save_emails

st.title(":orange[Contact]")

with st.form("Me contacter"):
    name = st.text_input("Votre Nom")
    email = st.text_input("Votre e-mail")
    message = st.text_area("Votre message")

    sent = st.form_submit_button("Envoyer")

    if sent:
        if check_informations(name, email, message):
            save_emails(name, email, message)
            st.balloons()
            st.toast("📬 Message envoyé !")
        else:
            st.error("Veuillez vérifier vos informations.")