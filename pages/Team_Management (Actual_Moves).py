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
######################## df8 #############################################################
df8 = pd.read_excel(File,'Team_Management')
df8.columns  = [i.replace(' ','_') for i in df8.columns]
df8.columns  = [i.upper() for i in df8.columns]
df8.dropna(axis=0, inplace=True)

df8["RIG_NO."]  = [i.replace(' ','') for i in df8["RIG_NO."]]
df8["JOB_TYPE"]  = [i.upper() for i in df8["JOB_TYPE"]]
df8["ACTUAL_DATE"]= pd.to_datetime(df8["ACTUAL_DATE"])
df8['ACTUAL_DATE']=df8['ACTUAL_DATE'].dt.strftime('%d-%m-%Y')
df8["RIG_ORDER"]=df8["RIG_ORDER"].astype("int") 
dict= {-1:"Previous",0:"Now",1:"Next"}
df8["RIG_ORDER"]=df8["RIG_ORDER"].map(dict)

Audit = df8[df8['AUDIT/DROPS']=="Audit"]
Drops = df8[df8['AUDIT/DROPS']=="Drops"]



st.image(image)
st.markdown(" <center>  <h1> Updated Actual Surveyed Rigs </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)


st.markdown(" <center>  <h1> Audit Team Timeline </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
RB1_list=list(Audit['TEAM_NO.'].unique())
RB1=st.radio("Audit Teams ",RB1_list)

Phases_Slider = st.select_slider('(Then >> Now >> Next) Audit Team Rigs', options=["Previous","Now", "Next"])

for i in range (0,len(RB1_list)):
            if RB1 == RB1_list[i]:
                        Audit_Team =  Audit[(Audit['TEAM_NO.']==RB1) & (Audit['RIG_ORDER']==Phases_Slider)]
                        Audit_Team.reset_index(inplace=True)
                        Audit_Team.drop(['TEAM_NO.','AUDIT/DROPS','index',"RIG_ORDER"], axis=1, inplace=True)
                        st.dataframe(Audit_Team,use_container_width=True) 

st.markdown(" <center>  <h1> Drops Team Timeline </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
RB2_list=list(Drops['TEAM_NO.'].unique())
RB2=st.radio("Drops Teams",RB2_list)
Phases_Sliderr = st.select_slider('(Then >> Now >> Next) Drops Team Rigs ', options=["Previous","Now", "Next"])


for i in range (0,len(RB2_list)):
            if RB2 == RB2_list[i]:
                        Drops_Team =  Drops[(Drops['TEAM_NO.']==RB2)&(Drops['RIG_ORDER']==Phases_Sliderr) ]
                        Drops_Team.reset_index(inplace=True)
                        Drops_Team.drop(["TEAM_NO.","AUDIT/DROPS","index","RIG_ORDER"], axis=1, inplace=True)
                        st.dataframe(Drops_Team,use_container_width=True) 

  


# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




