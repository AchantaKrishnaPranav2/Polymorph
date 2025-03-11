import streamlit as st

st.title("ELEMENTS")
st.sidebar.title("Properties")
st.header("Formula :red[B]:fire:",divider = True)
st.sidebar.header("Physical",divider = True)
st.sidebar.link_button("Click here for the code","https://krishnapranav.streamlit.app/")

st.radio("which element do you want to know about",["Boron","Carbon"])
st.button("submit")
