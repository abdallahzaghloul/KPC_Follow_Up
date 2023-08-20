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

df7["AUDIT/DROPS"]  = [i.replace(' ','') for i in df7["AUDIT/DROPS"]]
df7["AUDIT/DROPS"]  = [i.upper() for i in df7["AUDIT/DROPS"]]
df7["RIG"]  = [i.replace(' ','') for i in df7["RIG"]]
df7["RIG"]  = [i.upper() for i in df7["RIG"]]
df7["ARRIVAL_DATE"]= pd.to_datetime(df7["ARRIVAL_DATE"])
df7["DEPARTURE_DATE"]= pd.to_datetime(df7["DEPARTURE_DATE"])
df7['DAYS_COUNT'] = df7['DEPARTURE_DATE']-df7['ARRIVAL_DATE']

df7['ARRIVAL_DATE']=df7['ARRIVAL_DATE'].dt.strftime('%d-%m-%Y')
df7['DEPARTURE_DATE']=df7['DEPARTURE_DATE'].dt.strftime('%d-%m-%Y')
df7['DEPARTURE_DATE']=df7['DEPARTURE_DATE'].astype('str')
df7['ARRIVAL_DATE']=df7['ARRIVAL_DATE'].astype('str')
df7['DAYS_COUNT']=df7['DAYS_COUNT'].astype('str')

df7.reset_index(inplace=True)
df7.set_index('TEAM_NO.',  inplace=True)

Audit = df7[df7['AUDIT/DROPS']=="AUDIT"]
Drops = df7[df7['AUDIT/DROPS']=="DROPS"]



st.image(image)


st.markdown(" <center>  <h1> Audit Team Tracking </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

RB1=st.radio("What is Audit Team's Plan ",["Previously", "Now", "Next"])


if RB1 == "Previously":
            Audit_Previous =  Audit[Audit['JOB_STATE']==-1]
            Audit_Previous.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Audit_Previous=Audit_Previous.transpose()
            st.dataframe(Audit_Previous,use_container_width=True) 

elif RB1 == "Now":
            Audit_Now =  Audit[Audit['JOB_STATE']==0]
            Audit_Now.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Audit_Now=Audit_Now.transpose()
            st.dataframe(Audit_Now,use_container_width=True)             


elif RB1 == "Next":
            Audit_Next =  Audit[Audit['JOB_STATE']==1]
            Audit_Next.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Audit_Next=Audit_Next.transpose()
            st.dataframe(Audit_Next,use_container_width=True)

  
st.markdown(" <center>  <h1> Drops Team Tracking </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

RB2=st.radio("What is Drops Team's Plan ",["Previously", "Now", "Next"])


if RB2 == "Previously":
            Drops_Previous =  Drops[Drops['JOB_STATE']==-1]
            Drops_Previous.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Drops_Previous=Drops_Previous.transpose()
            st.dataframe(Drops_Previous,use_container_width=True) 

elif RB2 == "Now":
            Drops_Now =   Drops[Drops['JOB_STATE']==0]
            Drops_Now.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Drops_Now=Drops_Now.transpose()
            st.dataframe(Drops_Now,use_container_width=True)             


elif RB2 == "Next":
            Drops_Next =  Drops[Drops['JOB_STATE']==1]
            Drops_Next.drop(["JOB_STATE","AUDIT/DROPS","index"], axis= 1 , inplace= True)
#           Drops_Next=Drops_Next.transpose()
            st.dataframe(Drops_Next,use_container_width=True)

  




# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




