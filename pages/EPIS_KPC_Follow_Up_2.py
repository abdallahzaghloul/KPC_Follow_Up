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
df4['Final_Status']=df4['FINAL_\nSTATUS']
df4.drop(['PRIORITY','REF.','FINAL_\nSTATUS'],axis=1, inplace=True)
######################## df5 #############################################################

df5 = pd.read_excel(File,'phases')
df5.columns  = [i.replace(' ','_') for i in df5.columns]
df5.columns  = [i.upper() for i in df5.columns]

DRLG_Rigs=df4[df4['RIG_TYPE']=="DRLG"]['RIG_NO.'].unique()
DRLG_Rigs=tuple(DRLG_Rigs)
st.image(image)


st.markdown(" <center>  <h1> Drilling Open/In Progress Critical Points </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



st.markdown(" <right>  <h1> (I) Survey/Audit</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

DRLG_Phases=df5['PHASES'].unique()
DRLG_Phases=list(DRLG_Phases)

RB1=st.radio("Select an Active Rig: ",DRLG_Rigs)
Phases_Slider = st.select_slider('Select Phase', options=DRLG_Phases)

for i in range (0,len(DRLG_Rigs)):
            if RB1==DRLG_Rigs[i]:
                        st.write(f"Critical Points of Rig {DRLG_Rigs[i]} ")
                        All_Critical=df4[df4['RIG_NO.']==DRLG_Rigs[i]&df4['PHASE']==Phases_Slider]
                        All_Critical.drop(['LOCATION','RIG_NO.','RIG_TYPE','RIG_OWNER'],axis=1, inplace=True)
                        T1=st.dataframe(All_Critical,use_container_width=True)                                    




# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




