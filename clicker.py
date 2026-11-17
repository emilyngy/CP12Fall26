import streamlit as st

if 'click_score' not in st.session_state:
    st.session_state.click_score = 1
if "a" not in st.session_state:
    st.session_state.a = 0
if "upgd" not in st.session_state:
    st.session_state.upgd = 50

if st.button('click'):
    st.session_state.a += st.session_state.click_score
    st.rerun()

can_afford = st.session_state.a >= st.session_state.upgd

if st.button('upgrade (+1/click) - Cost: 50', disabled = not can_afford):
    st.session_state.a -= st.session_state.upgd
    st.session_state.click_score += 1
    st.rerun()

if st.button("play again"):
    st.session_state.a = 0
    st.session_state.click_score = 1
    st.session_state.upgd = 50
    st.rerun()

st.write("Score:", st.session_state.a)
st.write("Power per click:", st.session_state.click_score)