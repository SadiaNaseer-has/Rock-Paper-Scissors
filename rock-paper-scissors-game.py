import streamlit as st
import random

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = {'user': 0, 'computer': 0}

choices = ["rock 🎸", "paper 📄", "scissors ✂️"]
user_choice = st.selectbox("Choose your move:", choices)

if st.button("Play", type="primary"):
    comp_choice = random.choice(choices)
    
    # Determine winner
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
    
    st.write(f"*Your choice:* {user_choice}")
    st.write(f"*Computer's choice:* {comp_choice}")
    st.write(result)
    st.write(f"*Score - You:* {st.session_state.score['user']} | *Computer:* {st.session_state.score['computer']}")

if st.button("Reset Score"):
    st.session_state.score = {'user': 0, 'computer': 0}
    st.experimental_rerun()








