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


######################## df4 #############################################################
df4 = pd.read_excel(File,'All_Critical_Points')
df4.columns  = [i.replace(' ','_') for i in df4.columns]
df4.columns  = [i.upper() for i in df4.columns]
df4.dropna(axis=0, inplace=True)
df4.set_index('NO.', inplace=True)
df4.drop(['PRIORITY','REF.','FINAL_\nSTATUS'],axis=1, inplace=True)
All_Rigs=df4[df4['RIG_TYPE']=="DRLG"]['RIG_NO.'].unique()
All_Rigs=tuple(All_Rigs)
st.image(image)


st.markdown(" <center>  <h1> Drilling Open/In Progress Critical Points </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



st.markdown(" <right>  <h1> (I) Survey/Audit</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

RB1=st.radio("Select an Active Rig: ",All_Rigs)
for i in range (0,len(All_Rigs)):
            if RB1==All_Rigs[i]:
                        st.write(f"Critical Points of Rig {All_Rigs[i]} ")
                        All_Critical=df4[df4['RIG_NO.']==All_Rigs[i]]
                        All_Critical.drop(['LOCATION','RIG_NO.','PHASE','RIG_TYPE','RIG_OWNER'],axis=1, inplace=True)
                        T1=st.dataframe(All_Critical,use_container_width=True)                                    




# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




