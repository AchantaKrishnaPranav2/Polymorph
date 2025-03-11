import streamlit as st
import time
import pandas as pd
st.title("ELEMENTS")
st.sidebar.title("Properties")
st.sidebar.header("Physical",divider = False)
st.sidebar.link_button("Click here for the code","https://krishnapranav.streamlit.app/")

a = st.radio("Choose",[":red[B]  :fire:",":violet[K]  :sparkles:"],captions = ["Boron","Potassium"] ,index = None)
time.sleep(1)
if a == ":red[B]  :fire:" :
  st.write(":red[Boron] has the symbol B and atomic number 5",divider = True)
  time.sleep(1)
  st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Boron_R105.jpg/330px-Boron_R105.jpg",caption = "boron (β-rhombohedral)",width = 300)
  time.sleep(2)
  st.write("Molecular weight: 10.811", divider = True)
  time.sleep(3)
  df = pd.DataFrame(
    {
        "name": ["dark ,Lustrous , Brittle, Metalloid"],
        "url": ["Brown Powder"],
    }
  )
  st.dataframe(
    df,
    column_config={
        "name": "Crystalline Form",
        
        "url": "Amorphous Form",
       
    },width =400,
    height = 50,
    hide_index=True,
  )
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  


