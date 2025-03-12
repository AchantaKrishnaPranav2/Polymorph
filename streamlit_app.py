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

  # Create DataFrame from given data
  data = {
      "Temperature (K)": [4138, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000,
                          5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000],
      "Cp (J/mol*K)": [20.86, 20.87, 20.89, 20.91, 20.94, 20.96, 20.99, 21.02, 21.05, 21.09,
                       21.13, 21.17, 21.21, 21.26, 21.31, 21.36, 21.42, 21.48, 21.55, 21.61],
      "S° (J/mol*K)": [208.1, 208.4, 208.9, 209.4, 209.9, 210.3, 210.8, 211.2, 211.7, 212.1,
                       212.5, 212.9, 213.3, 213.7, 214.1, 214.5, 214.9, 215.2, 215.6, 216.0],
      "-(G° - H°298.15)/T (J/mol*K)": [188.8, 189.1, 189.6, 190.0, 190.4, 190.9, 191.3, 191.7, 192.1, 192.5,
                                       192.9, 193.3, 193.6, 194.0, 194.4, 194.7, 195.1, 195.4, 195.8, 196.1],
      "H° - H°298.15 (kJ/mol)": [79.84, 81.14, 83.23, 85.32, 87.41, 89.50, 91.60, 93.70, 95.81, 97.91,
                                 100.0, 102.1, 104.3, 106.4, 108.5, 110.6, 112.8, 114.9, 117.1, 119.2]
  }
  
  df = pd.DataFrame(data)
  
  # Streamlit app
  st.title("Thermodynamic Properties Visualization")
  
  # Line chart
  st.line_chart(df.set_index("Temperature (K)"))
   
  
  


