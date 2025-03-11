import streamlit as st
import time
st.title("ELEMENTS")
st.sidebar.title("Properties")
st.header("Formula :red[B]:fire:",divider = True)
st.sidebar.header("Physical",divider = True)
st.sidebar.link_button("Click here for the code","https://krishnapranav.streamlit.app/")

a = st.radio("Choose",["B","K"],captions = ["Boron","Potassium"] ,index = None)
time.sleep(1)
if a == "B":
  st.text(":violet[Boron] has the symbol B and atomic number 5")
  st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Boron_R105.jpg")
  time.sleep(2)
  st.text("Molecular weight: 10.811")
  


