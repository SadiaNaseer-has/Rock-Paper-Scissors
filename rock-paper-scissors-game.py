import streamlit as st
import random

# Page config
st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="🪨", layout="centered")

# Header
st.markdown("<h1 style='text-align: center;'>🪨 Rock-Paper-Scissors Game</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = {'user': 0, 'computer': 0}

# Game container
with st.container():
    st.subheader("Play the Game")
    col1, col2 = st.columns(2)
    with col1:
        user_choice = st.selectbox("Choose your move", ["rock 🎸", "paper 📄", "scissors ✂️"])
        if st.button("Play", type="primary"):
            comp_choice = random.choice(["rock 🎸", "paper 📄", "scissors ✂️"])
            
            # Determine winner
            choices = ["rock 🎸", "paper 📄", "scissors ✂️"]
            user_move = choices.index(user_choice)
            comp_move = choices.index(comp_choice)
            
            if user_move == comp_move:
                result = "It's a tie!"
            elif (user_move - comp_move) % 3 == 1:
                result = "You win!"
                st.session_state.score['user'] += 1
            else:
                result = "Computer wins!"
                st.session_state.score['computer'] += 1
            
            st.write(f"Your choice: {user_choice}")
            st.write(f"Computer's choice: {comp_choice}")
            st.write(result)
    with col2:
        st.subheader("Scoreboard")
        st.write(f"*You:* {st.session_state.score['user']}")
        st.write(f"*Computer:* {st.session_state.score['computer']}")

st.markdown("---")
if st.button("Reset Score"):
    st.session_state.score = {'user': 0, 'computer': 0}
    st.experimental_rerun()
