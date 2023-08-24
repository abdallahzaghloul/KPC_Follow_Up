#Tog1 = st.selectbox("Desired Model Selection ",(' A1', ' A6', ' A4', ' A3' ,' Q3', ' Q5', ' A5' ,' S4', ' Q2', ' A7', ' TT', ' Q7',' RS6' ,' RS3', ' A8' ,' Q8' ,' RS4', ' RS5' ,' R8', ' SQ5', ' S8', ' SQ7', ' S3',' S5' ,' A2', ' RS7'))
#Y=st.slider('Select the year you are interested in',1997,2020)

import math
from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
File="Client_EPIS_Daily_Progress.xlsx"
im = Image.open("EPIS.png")
image = np.array(im)
######################## df7 #############################################################
df7 = pd.read_excel(File,'Plan')
df7.columns  = [i.replace(' ','_') for i in df7.columns]
df7.columns  = [i.upper() for i in df7.columns]
df7.dropna(axis=0, inplace=True)

df7["RIG_NO."]  = [i.replace(' ','') for i in df7["RIG_NO."]]
df7["JOB_TYPE"]  = [i.upper() for i in df7["JOB_TYPE"]]
df7["EXPECTED_DATE"]= pd.to_datetime(df7["EXPECTED_DATE"])
df7['EXPECTED_DATE']=df7['EXPECTED_DATE'].dt.strftime('%d-%m-%Y')

df7['RIG_ORDER']=df7['RIG_ORDER'].astype('str')

df7['RIG_ORDER']="Rig_"+df7['RIG_ORDER']
Audit = df7[df7['AUDIT/DROPS']=="Audit"]
Drops = df7[df7['AUDIT/DROPS']=="Drops"]



st.image(image)
st.markdown(" <center>  <h1> Monthly Plan </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

st.markdown(" <center>  <h1> Audit Team Tracking </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
RB1_list=list(Audit['TEAM_NO.'].unique())
RB1=st.radio("What is Audit Team's Plan ",RB1_list)


for i in range (0,len(RB1_list)):
            if RB1 == RB1_list[i]:
                        Audit_Team =  Audit[Audit['TEAM_NO.']==RB1]
                        Audit_Team.reset_index(inplace=True)
                        Audit_Team.drop(['TEAM_NO.','AUDIT/DROPS','index'], axis=1, inplace=True)
                        st.dataframe(Audit_Team,use_container_width=True) 

st.markdown(" <center>  <h1> Drops Team Tracking </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
RB2_list=list(Drops['TEAM_NO.'].unique())
RB2=st.radio("What is Drops Team's Plan ",RB2_list)


for i in range (0,len(RB2_list)):
            if RB2 == RB2_list[i]:
                        Drops_Team =  Drops[Drops['TEAM_NO.']==RB2]
                        Drops_Team.reset_index(inplace=True)
                        Drops_Team.drop(['TEAM_NO.','AUDIT/DROPS','index'], axis=1, inplace=True)
                        st.dataframe(Drops_Team,use_container_width=True) 

  


# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




