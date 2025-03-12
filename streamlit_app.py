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
  st.subheader("Electronic configuration :")
  st.latex("2s^2 2p^1 ")

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Group", "13")
  col2.metric("Period", "2")
  col3.metric("Block", "P-block")
  
  
  # Create DataFrame
  data = {
      "Temperature (K)": [4138, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000,
                          5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000],
      "Cp*100 (J/mol*K)": [2086, 2087, 2089, 2091, 2094, 2096, 2099, 2102, 2105, 2109,
                       2113, 2117, 2121, 2126, 2131, 2136, 2142, 2148, 2155, 2161]
  }
  
  df = pd.DataFrame(data)
  
  
  
  
  
  st.title("Cp*100 vs Temperature (Filtered Range)")
  
  # Line chart for filtered Cp vs Temperature
  st.line_chart(df.set_index("Temperature (K)")["Cp*100 (J/mol*K)"])

     
  
  


