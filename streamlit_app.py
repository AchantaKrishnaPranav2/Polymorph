import streamlit as st
import time
import pandas as pd

st.title("ELEMENTS")
st.sidebar.title("Properties")
st.sidebar.header("Physical", divider=False)
st.sidebar.link_button("Click here for the code", "https://krishnapranav.streamlit.app/")

a = st.radio("Choose", [":red[B]  :fire:", ":violet[K]  :sparkles:"], captions=["Boron", "Potassium"], index=None)
time.sleep(1)

if a == ":red[B]  :fire:":
    st.write(":red[Boron] has the symbol B and atomic number 5", divider=True)
    time.sleep(1)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Boron_R105.jpg/330px-Boron_R105.jpg",
             caption="Boron (β-rhombohedral)", width=300)
    time.sleep(4)
    st.subheader("Molecular weight: 10.811", divider=True)
    time.sleep(4)
    
    df = pd.DataFrame(
        {
            "name": ["Dark, Lustrous, Brittle, Metalloid"],
            "url": ["Brown Powder"],
        }
    )
    
    st.dataframe(
        df,
        column_config={
            "name": "Crystalline Form",
            "url": "Amorphous Form",
        },
        width=400,
        height=100,
        hide_index=True,
    )
    time.sleep(2)
    st.subheader("Electronic Configuration:")
    st.latex("2s^2 2p^1 ")
    time.sleep(1)
    col1, col2, col3 = st.columns(3)
    col1.metric("Group", "13")
    col2.metric("Period", "2")
    col3.metric("Block", "P-block")
    time.sleep(1)
    
    option = st.selectbox(
    "Heat Capacity",
    ("Gas Phase", "Liquid Phase", "Solid Phase"), index = None
    )
    
    if option == "Gas Phase":
        
        st.subheader("Gas Phase Heat Capacity (Shomate Equation)")
        st.latex("Cp° = A + B*t^1 + C*t^2 + D*t^3 + E/t^2")
        st.write("A	= 20.65193\n B = 0.226427\n C =	-0.112330\n D =	0.016889\n E = 0.008714")
        
        # Create DataFrame (Ordered by Temperature)
        data = {
            "Temperature (K)": [4138, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000,
                                5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000],
            "Cp*100 (J/mol*K)": [2086, 2087, 2089, 2091, 2094, 2096, 2099, 2102, 2105, 2109,
                                 2113, 2117, 2121, 2126, 2131, 2136, 2142, 2148, 2155, 2161]
        }
    
        df = pd.DataFrame(data)
    
        # Sort data by Temperature (just to ensure correct order)
        df = df.sort_values(by="Temperature (K)", ascending=True)
    
        time.sleep(5)
    
        st.subheader("Cp*100 vs Temperature  for Boron in gaseous state")
    
        # Line chart for Cp vs Temperature (Ordered)
        st.line_chart(df.set_index("Temperature (K)")["Cp*100 (J/mol*K)"], height=400)


    elif option == "Liquid Phase":
        # Data
        data = {
            "Temperature (K)": [2350, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100],
            "Cp*100 (J/mol*K)": [3175] * 19,
            
        }
        
        # Create DataFrame
        df = pd.DataFrame(data)
        st.subheader("Liquid Phase Heat Capacity (Shomate Equation)")
        st.latex("Cp° = A + B*t + C*t^2 + D*t^3 + E/t^2")
        st.write("A = 31.75003 B = 2.556177×10-7 C = -6.456792×10-8 D = 5.616644×10-9 E = 2.705970×10-7")
        # Streamlit app
        st.subheader("Cp*100 vs Temperature in Liquid state")    
        df = df.sort_values(by="Temperature (K)", ascending=True)
        st.line_chart(df.set_index("Temperature (K)")["Cp*100 (J/mol*K)"], height=400)
    
    elif option == "Solid Phase":   
        data = {
            "Temperature (K)": [
                298, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,1800,
                1900, 2000, 2100, 2200, 2300
            ],
            "Cp*100 (J/mol*K)": [
                11.21, 11.33, 15.83, 18.63, 20.62, 22.15, 23.34, 24.30, 25.07, 25.70, 26.22, 26.68, 27.08,
                27.48, 27.88, 28.32,28.83, 28.73, 29.10, 29.45, 29.80, 30.14, 30.48
            ]
            }
            
        df = pd.DataFrame(data)
            
        # Sort data by Temperature (just to ensure correct order)
        df = df.sort_values(by="Temperature (K)", ascending=True)
        
        time.sleep(5)
        st.subheader("Solid Phase Heat Capacity (Shomate Equation)")
        st.latex("Cp° = A + B*t + C*t^2 + D*t^3 + E/t^2")
        
        st.write(" 298 K to 1800 K ")
        st.write("A = 10.18574  B = 29.24415 C = -18.02137 D = 4.212326 E = -0.550999")
        st.write("1800 K to 2350 K ")
        st.write("A = 25.12664 B = 1.975493 C = 0.338395 D = -0.040032 E = -2.635578")
        # Streamlit app
        st.subheader("Cp*100 vs Temperature in Solid state")    
        
        # Line chart for properties vs Temperature
        st.line_chart(df.set_index("Temperature (K)")["Cp*100 (J/mol*K)"], height=400)    
        
      
         
      
  


