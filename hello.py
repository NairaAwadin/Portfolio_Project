import streamlit as st

# print("run")  # 3 times, streamlit relance la page à chaque changement, donc une premiere fois quand on execute le fichier, ensuite quand on met notre prenom, et encore quand on le change
st.title("Hello")
name = st.text_input("What is your name?")
if name:
    st.write(f"Nice to meet you, {name}.")

age = st.slider("How old are you?", 15, 70, 20)
st.write("Your age is", age)

if age < 30:
    st.write("You will be 30 in", 30 - age, "years.")
else:
    st.write("You are old")
