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
######################## df1 #############################################################
df1 = pd.read_excel(File,'Audit_Teams_Follow_Up')
df1.columns  = [i.replace(' ','_') for i in df1.columns]
df1.columns  = [i.upper() for i in df1.columns]
df1.dropna(axis=0, inplace=True)
df1['RIG_NO.']  = [i.replace(' ','') for i in df1['RIG_NO.']]
df1['RIG_NO.']  = [i.upper() for i in df1['RIG_NO.']]
df1['JOB_TYPE']  = [i.replace(' ','') for i in df1['JOB_TYPE']]
df1['JOB_TYPE']  = [i.upper() for i in df1['JOB_TYPE']]

######################## df4 #############################################################
df4 = pd.read_excel(File,'All_Critical_Points')
df4.columns  = [i.replace(' ','_') for i in df4.columns]
df4.columns  = [i.upper() for i in df4.columns]
df4.dropna(axis=0, inplace=True)

df4['RIG_NO.']  = [i.replace(' ','') for i in df4['RIG_NO.']]
df4['RIG_NO.']  = [i.upper() for i in df4['RIG_NO.']]
df4['PHASE']  = [i.replace(' ','') for i in df4['PHASE']]
df4['PHASE']  = [i.upper() for i in df4['PHASE']]

df4['FINAL_STATUS']=df4['FINAL_\nSTATUS']
df4.drop(['PRIORITY','REF.','FINAL_\nSTATUS'],axis=1, inplace=True)



Omit_Rigs=tuple(df1['RIG_NO.'].unique())

df4.drop(df4[df4['RIG_NO.'].isin  (Omit_Rigs)].index,axis=0, inplace=True)


DRLG_Rigs=df4[df4['RIG_TYPE']=="DRLG"]['RIG_NO.'].unique()
DRLG_Rigs=tuple(DRLG_Rigs)

WO_Rigs=df4[df4['RIG_TYPE']=="WO"]['RIG_NO.'].unique()
WO_Rigs=tuple(WO_Rigs)


PU_Rigs=df4[df4['RIG_TYPE']=="PU"]['RIG_NO.'].unique()
PU_Rigs=tuple(PU_Rigs)




######################## df5 #############################################################

df5 = pd.read_excel(File,'phases')
df5.columns  = [i.replace(' ','_') for i in df5.columns]
df5.columns  = [i.upper() for i in df5.columns]
df5.dropna(axis=0, inplace=True)

df5['PHASES']  = [i.replace(' ','') for i in df5['PHASES']]
df5['PHASES']  = [i.upper() for i in df5['PHASES']]

######################## df6 #############################################################

df6 = pd.read_excel(File,'Phase_Dates')
df6.columns  = [i.replace(' ','_') for i in df6.columns]
df6.columns  = [i.upper() for i in df6.columns]
df6.dropna(axis=0, inplace=True)
df6['RIG_NO.']  = [i.replace(' ','') for i in df6['RIG_NO.']]
df6['RIG_NO.']  = [i.upper() for i in df6['RIG_NO.']]
df6['PHASE']  = [i.replace(' ','') for i in df6['PHASE']]
df6['PHASE']  = [i.upper() for i in df6['PHASE']]


#df6['DATE']=df6['DATE'].astype(str)
#df6['DATE']=df6['DATE'].str.split(' ').str[0]
df6["DATE"]= pd.to_datetime(df6["DATE"])
df6['TODAY_DATE']=datetime.date.today()
df6["TODAY_DATE"]= pd.to_datetime(df6["TODAY_DATE"])
df6['DAYS_COUNT'] = df6.TODAY_DATE-df6.DATE
df6.drop('TODAY_DATE',axis=1,inplace=True)
df6['DATE']=df6['DATE'].dt.strftime('%d-%m-%Y')
df6['DAYS_COUNT']=df6['DAYS_COUNT'].astype('str')
df6['DAYS_COUNT']=df6['DAYS_COUNT'].str.split(' ').str[0]


st.image(image)


st.markdown(" <center>  <h1> Drilling Open/In Progress Critical Points </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



#st.markdown(" <right>  <h1> (I) Survey/Audit</h1> </font> </right> </h1> ",
#            unsafe_allow_html=True)

DRLG_Phases=df5['PHASES'].unique()
DRLG_Phases=list(DRLG_Phases)

RB1=st.radio("Select DRLG Rig: ",DRLG_Rigs)
Phases_Slider = st.select_slider('Select DRLG Phase', options=DRLG_Phases)

for i in range (0,len(DRLG_Rigs)):
            if (RB1==DRLG_Rigs[i]) and (Phases_Slider=="ALL"):
                        All_Critical=df4[(df4['RIG_NO.']==DRLG_Rigs[i])]
                        All_Critical.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Critical=All_Critical.set_index("NO.")
                        T1=st.dataframe(All_Critical,use_container_width=True)
                      
                       

            if (RB1==DRLG_Rigs[i]) and (Phases_Slider!="ALL"):                       
                        All_Critical=df4[(df4['RIG_NO.']==DRLG_Rigs[i])&(df4['PHASE']==Phases_Slider)]
                        All_Critical.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Critical=All_Critical.set_index("NO.")
                        T1=st.dataframe(All_Critical,use_container_width=True)

Rig_Phase_1=list(df4[(df4["RIG_NO."]==RB1)]['PHASE'])
if (Phases_Slider!="ALL"):
  if Phases_Slider in Rig_Phase_1:
    st.write(f"Critical Points of Rig {RB1} ")
    Day_Count=list(df6[(df6["RIG_NO."]==RB1)&(df6['PHASE']==Phases_Slider)]['DAYS_COUNT'])
    Day_Count=float(Day_Count[0])
    Years=math.floor(Day_Count/365)
    Months=math.floor(12*(np. remainder(Day_Count/365,1))) 
    Days=round (30*(np. remainder(12*(np. remainder(Day_Count/365,1)),1)),0) 
    V=len(list(df4[(df4["RIG_NO."]==RB1)&(df4['PHASE']==Phases_Slider)]['PHASE']))
    st.write(f"Total Points of Rig {RB1} @ {Phases_Slider}  = {V} Points")
    st.write(f"These points were open since {Years} Years {Months} Months {Days} Days")  
  elif Phases_Slider not in Rig_Phase_1:
    st.write(f"There were no registered points @ {Phases_Slider} ")            
elif  (Phases_Slider=="ALL"):
            if list(df4[(df4["RIG_NO."]==RB1)]['PHASE'])==["NOCRITICAL"]:
                        st.write(f"There were no registered points @ All ")   
            elif list(df4[(df4["RIG_NO."]==RB1)]['PHASE'])!=["NOCRITICAL"] :
                         st.write(f"Critical Points of Rig {RB1} ")
                         V=len(list(df4[(df4["RIG_NO."]==RB1)]['PHASE']))
                         st.write(f"Total Points of Rig {RB1} = {V} Points")
st.write(f"The Carried on Phases{list((df6[df6['RIG_NO.']==RB1]['PHASE']).unique())}")
  
  

st.markdown(" <center>  <h1> WO Open/In Progress Critical Points </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)


WO_Phases=df5['PHASES'].unique()
WO_Phases=list(WO_Phases)

RB2=st.radio("SelectWO Rig: ",WO_Rigs)
Phases_Sliderr = st.select_slider('Select Phase WO', options=WO_Phases)

for ii in range (0,len(WO_Rigs)):
            if (RB2==WO_Rigs[ii]) and (Phases_Sliderr=="ALL"):
                        st.write(f"Critical Points of Rig {WO_Rigs[ii]} ")
                        All_Criticall=df4[(df4['RIG_NO.']==WO_Rigs[ii])]
                        All_Criticall.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Criticall=All_Criticall.set_index("NO.")
                        T1=st.dataframe(All_Criticall,use_container_width=True)    
            if (RB2==WO_Rigs[ii]) and (Phases_Sliderr!="ALL"):
                        st.write(f"Critical Points of Rig {WO_Rigs[ii]} ")
                        All_Criticall=df4[(df4['RIG_NO.']==WO_Rigs[ii])&(df4['PHASE']==Phases_Sliderr)]
                        All_Criticall.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Criticall=All_Criticall.set_index("NO.")
                        T1=st.dataframe(All_Criticall,use_container_width=True)                                    

Rig_Phase_2=list(df4[(df4["RIG_NO."]==RB2)]['PHASE'])
if (Phases_Sliderr!="ALL"):
  if Phases_Sliderr in Rig_Phase_2:
    st.write(f"Critical Points of Rig {RB2} ")
    Day_Count=list(df6[(df6["RIG_NO."]==RB2)&(df6['PHASE']==Phases_Sliderr)]['DAYS_COUNT'])
    Day_Count=float(Day_Count[0])
    Years=math.floor(Day_Count/365)
    Months=math.floor(12*(np. remainder(Day_Count/365,1))) 
    Days=round (30*(np. remainder(12*(np. remainder(Day_Count/365,1)),1)),0) 
    VV=len(list(df4[(df4["RIG_NO."]==RB2)&(df4['PHASE']==Phases_Sliderr)]['PHASE']))
    st.write(f"Total Points of Rig {RB2} @ {Phases_Sliderr}  = {VV} Points")
    st.write(f"These points were open since {Years} Years {Months} Months {Days} Days")
  elif Phases_Sliderr not in Rig_Phase_2:
    st.write(f"There were no registered points @ {Phases_Sliderr} ")
    
elif  (Phases_Sliderr=="ALL"):
            if list(df4[(df4["RIG_NO."]==RB2)]['PHASE'])==["NOCRITICAL"]:
                        st.write(f"There were no registered points @ All ")   
            elif list(df4[df4["RIG_NO."]==RB2]['PHASE'])!=["NOCRITICAL"] :
                        st.write(f"Critical Points of Rig {RB2} ")
                        VV=len(list(df4[(df4["RIG_NO."]==RB2)]['PHASE']))
                        st.write(f"Total Points of Rig {RB2} = {VV} Points")

st.write(f"The Carried on Phases{list((df6[df6['RIG_NO.']==RB2]['PHASE']).unique())}")

st.markdown(" <center>  <h1> PU Open/In Progress Critical Points </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

PU_Phases=df5['PHASES'].unique()
PU_Phases=list(PU_Phases)

RB3=st.radio("Select PU : ",PU_Rigs)
Phases_Sliderrr = st.select_slider('Select Phase PU', options=PU_Phases)

for iii in range (0,len(PU_Rigs)):
            if (RB3==PU_Rigs[iii]) and (Phases_Sliderrr=="ALL"):
                        st.write(f"Critical Points of Rig {PU_Rigs[iii]} ")
                        All_Criticalll=df4[(df4['RIG_NO.']==PU_Rigs[iii])]
                        All_Criticalll.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Criticalll=All_Criticalll.set_index("NO.")
                        T1=st.dataframe(All_Criticalll,use_container_width=True)    
            if (RB3==PU_Rigs[iii]) and (Phases_Sliderrr!="ALL"):
                        st.write(f"Critical Points of Rig {PU_Rigs[iii]} ")
                        All_Criticalll=df4[(df4['RIG_NO.']==PU_Rigs[iii])&(df4['PHASE']==Phases_Sliderrr)]
                        All_Criticalll.drop(['LOCATION','RIG_NO.','RIG_TYPE'],axis=1, inplace=True)
                        All_Criticalll=All_Criticalll.set_index("NO.")
                        T1=st.dataframe(All_Criticalll,use_container_width=True)                                    


Rig_Phase_3=list(df4[(df4["RIG_NO."]==RB3)]['PHASE'])
if (Phases_Sliderrr!="ALL"):
  if Phases_Sliderrr in Rig_Phase_3:
    st.write(f"Critical Points of Rig {RB3} ")
    Day_Count=list(df6[(df6["RIG_NO."]==RB3)&(df6['PHASE']==Phases_Sliderrr)]['DAYS_COUNT'])
    Day_Count=float(Day_Count[0])
    Years=math.floor(Day_Count/365)
    Months=math.floor(12*(np. remainder(Day_Count/365,1))) 
    Days=round (30*(np. remainder(12*(np. remainder(Day_Count/365,1)),1)),0) 
    VVV=len(list(df4[(df4["RIG_NO."]==RB3)&(df4['PHASE']==Phases_Sliderrr)]['PHASE']))
    st.write(f"Total Points of Rig {RB3} @ {Phases_Sliderrr}  = {VVV} Points")
    st.write(f"These points were open since {Years} Years {Months} Months {Days} Days")
  elif Phases_Sliderrr not in Rig_Phase_3:
    st.write(f"There were no registered points @ {Phases_Sliderrr}")
    
elif  (Phases_Sliderrr=="ALL"):
            if list(df4[(df4["RIG_NO."]==RB3)]['PHASE'])==["NOCRITICAL"]:
                        st.write(f"There were no registered points @ All ")   
            elif list(df4[df4["RIG_NO."]==RB3]['PHASE'])!=["NOCRITICAL"] :
                        st.write(f"Critical Points of Rig {RB3} ")
                        VVV=len(list(df4[(df4["RIG_NO."]==RB3)]['PHASE']))
                        st.write(f"Total Points of Rig {RB3} = {VVV} Points")

st.write(f"The Carried on Phases{list((df6[df6['RIG_NO.']==RB3]['PHASE']).unique())}")








# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




