#Tog1 = st.selectbox("Desired Model Selection ",(' A1', ' A6', ' A4', ' A3' ,' Q3', ' Q5', ' A5' ,' S4', ' Q2', ' A7', ' TT', ' Q7',' RS6' ,' RS3', ' A8' ,' Q8' ,' RS4', ' RS5' ,' R8', ' SQ5', ' S8', ' SQ7', ' S3',' S5' ,' A2', ' RS7'))
#Y=st.slider('Select the year you are interested in',1997,2020)


from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
File="Client_EPIS_Daily_Progress.xlsx"
im = Image.open("EPIS.png")
image = np.array(im)


######################## df1 #############################################################
df8 = pd.read_excel(File,'Rig_Mast_Problems_Drops')
df8.columns  = [i.replace(' ','_') for i in df8.columns]
df8.columns  = [i.upper() for i in df8.columns]
df8["RIG_NO."]  = [i.upper() for i in df8["RIG_NO."]]
df8["RIG_TYPE"]  = [i.upper() for i in df8["RIG_TYPE"]]
df8["RIG_NO."]  =df8["RIG_NO."] .str.strip()
df8["RIG_TYPE"]  =df8["RIG_TYPE"] .str.strip()
df8.dropna(axis=0,inplace=True)
df8['NO.'] = df8["RIG_NO."].str.split("-").str[-1]
df8['NO.']= df8['NO.'].astype("int")
df8=df8.sort_values(by='NO.', ascending=True)
df8.drop('NO.', inplace=True, axis=1)
df8.set_index("RIG_NO.", inplace=True)
df8.head(10)







st.image(image)

 



st.markdown(" <center>  <h1> Rigs with Mast Problems </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

DRLG_MAST = df8[df8["RIG_TYPE"]=="DRLG"]
WO_MAST = df8[df8["RIG_TYPE"]=="WO"]
PU_MAST = df8[df8["RIG_TYPE"]=="PU"]




st.markdown(" <right>  <h1> (I) DRLG Rigs</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

st.dataframe(DRLG_MAST)

st.markdown(" <right>  <h1> (I) WO Rigs</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

st.dataframe(WO_MAST)

st.markdown(" <right>  <h1> (I) PU Rigs</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

st.dataframe(PU_MAST)



# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




