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
  st.text(":voilet[Boron] has the symbol B and atomic number 5")
  st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Boron_R105.jpg/330px-Boron_R105.jpg",caption = "boron (β-rhombohedral)",width = 200)
  time.sleep(2)
  st.text("Molecular weight: 10.811")
  


