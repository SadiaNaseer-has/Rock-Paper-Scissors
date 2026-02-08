import streamlit as st
import random

st.title("Rock-Paper-Scissors Game")

user_choice = st.selectbox("Choose:", ["rock", "paper", "scissors"])

if st.button("Play"):
    comp_choice = random.choice(["rock", "paper", "scissors"])
    st.write(f"Computer chose: *{comp_choice}*")
    
    if user_choice == comp_choice:
        st.write("👉 *Tie!*")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        st.write("👉 *You win!*")
    else:
        st.write("👉 *You lose!*")

st.write("---")
if st.button("Reset"):
    st.experimental_rerun()
