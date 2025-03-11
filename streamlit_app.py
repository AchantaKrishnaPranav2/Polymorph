import streamlit as st

st.title("ELEMENTS")
st.sidebar.title("Properties")
st.header("Formula :red[B]:fire:",divider = True)
st.sidebar.header("Physical",divider = True)
st.sidebar.link_button("Click here for the code","https://krishnapranav.streamlit.app/")

a = st.radio("Choose",["B","K"],captions = ["Boron","Potassium"] ,index = None)


