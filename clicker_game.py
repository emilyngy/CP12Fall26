import streamlit as st

st.header("Clicker Game")

if 'click_score' not in st.session_state:
    st.session_state.click_score = 1
if "a" not in st.session_state:
    st.session_state.a = 0
if "upgd" not in st.session_state:
    st.session_state.upgd = 50

if st.session_state.click_score < 3:
    img_url = "https://em-content.zobj.net/source/apple/391/cookie_1f36a.png"
    rank_name = "Level 1"
elif st.session_state.click_score < 6:
    img_url = "https://em-content.zobj.net/source/apple/391/shortcake_1f370.png"
    rank_name = "Level 2"
else:
    img_url = "https://em-content.zobj.net/source/apple/391/gem-stone_1f48e.png"
    rank_name = "Level 3"

img, info = st.columns([1, 2])

with img:
    st.image(img_url, width=140)

with info:
    st.subheader(rank_name)
    st.metric(label="Score", value=st.session_state.a)
    st.metric(label="Power/click", value=f"+{st.session_state.click_score}")

st.divider()

if st.button('click'):
    st.session_state.a += st.session_state.click_score
    st.rerun()

can_afford = st.session_state.a >= st.session_state.upgd

upg, reset = st.columns(2)
with upg:
    if st.button('upgrade (+1/click) - Cost: 50', disabled = not can_afford):
        st.session_state.a -= st.session_state.upgd
        st.session_state.click_score += 1
        st.rerun()

with reset:
    if st.button("play again"):
        st.session_state.a = 0
        st.session_state.click_score = 1
        st.session_state.upgd = 50
        st.rerun()