import streamlit as st
import random

# Page config
st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="🎮", layout="centered")

# Header
st.title("🎮 Rock-Paper-Scissors")
st.markdown(" a simple game of chance")                                          
if 'score' not in st.session_state:
    st.session_state.score = {'user': 0, 'computer': 0}

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.subheader("### A simple game of chance")

# Score tracker
if 'score' not in st.session_state:
    st.session_state.score = {'user': 0, 'computer': 0}

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st.subheader("You")
    st.write(f"Score: *{st.session_state.score['user']}*")
with col2:
    st.write("")
with col3:
    st.subheader("Computer")
    st.write(f"Score: *{st.session_state.score['computer']}*")

            
user_choice = st.selectbox("# Game logic")
user_choice = st.selectbox("Choose your move:", ["rock 🎸", "paper 📄", "scissors ✂️"])

if st.button("Play", type="primary"):
    comp_choice = random.choice(["rock 🎸", "paper 📄", "scissors ✂️"])
    
                      
    if user_choice == comp_choice:
        result = "# Determine winner
    if user_choice == comp_choice:
        result = "Tie!"
    elif (user_choice == "rock 🎸" and comp_choice == "scissors ✂️") or \
         (user_choice == "paper 📄" and comp_choice == "rock 🎸") or \
         (user_choice == "scissors ✂️" and comp_choice == "paper 📄"):
        st.session_state.score['user'] += 1
        result = "You win!"
    else:
        st.session_state.score['computer'] += 1
        result = "Computer wins!"

                 
    st.write(f"# Show result
    st.write(f"Computer chose: *{comp_choice}*")
    st.subheader(result)

       
if st.button("# Reset
if st.button("Reset Score"):
    st.session_state.score = {'user': 0, 'computer': 0}
    st.experimental_rerun()



