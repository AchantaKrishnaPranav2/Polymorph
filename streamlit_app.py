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
      "Cp (J/mol*K)": [20.86, 20.87, 20.89, 20.91, 20.94, 20.96, 20.99, 21.02, 21.05, 21.09,
                       21.13, 21.17, 21.21, 21.26, 21.31, 21.36, 21.42, 21.48, 21.55, 21.61]
  }
  
  df = pd.DataFrame(data)
  
  # Define filter range
  cp_min, cp_max = 20.8, 21.7
  
  # Filter data for Cp within range
  df_filtered = df[(df["Cp (J/mol*K)"] >= cp_min) & (df["Cp (J/mol*K)"] <= cp_max)]
  
  # Ensure filtered data is not empty
  if df_filtered.empty:
      st.warning(f"No data points found in the range {cp_min} to {cp_max}.")
  else:
      # Streamlit app
      st.title("Cp vs Temperature (Filtered Range)")
  
      # Line chart for filtered Cp vs Temperature
      st.line_chart(df_filtered.set_index("Temperature (K)")["Cp (J/mol*K)"],height = 100)

     
  
  


