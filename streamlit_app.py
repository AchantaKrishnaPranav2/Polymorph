import streamlit as st
import time
st.title("ELEMENTS")
st.sidebar.title("Properties")
st.sidebar.header("Physical",divider = True)
st.sidebar.link_button("Click here for the code","https://krishnapranav.streamlit.app/")

a = st.radio("Choose",[":red[B]:fire:",":violet[K]:sparkles:"],captions = ["Boron","Potassium"] ,index = None)
time.sleep(1)
if a == "B":
  st.write(":red[Boron] has the symbol B and atomic number 5")
  time.sleep(1)
  st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Boron_R105.jpg/330px-Boron_R105.jpg",caption = "boron (β-rhombohedral)",width = 300)
  time.sleep(2)
  st.text("Molecular weight: 10.811")
  time.sleep(1)
  st.write(" In its crystalline form it is a brittle, dark,lustrous :grey[metalloid]")
  


