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
df1 = pd.read_excel(File,'Audit_Teams_Follow_Up')
df1.columns  = [i.replace(' ','_') for i in df1.columns]
df1.columns  = [i.upper() for i in df1.columns]
df1.dropna(axis=0, inplace=True)

df1['RIG_NO.']  = [i.replace(' ','') for i in df1['RIG_NO.']]
df1['RIG_NO.']  = [i.upper() for i in df1['RIG_NO.']]
df1['JOB_TYPE']  = [i.replace(' ','') for i in df1['JOB_TYPE']]
df1['JOB_TYPE']  = [i.upper() for i in df1['JOB_TYPE']]

Inv="INCIDENT_INVESTIGATION"
Alert=0
Z=pd.DataFrame()

df1['TODAY_DATE']=datetime.date.today()
df1['STARTING_DATE']=df1['STARTING_DATE'].astype(str)
df1['STARTING_DATE']=df1['STARTING_DATE'].str.split(' ').str[0]
df1["STARTING_DATE"]= pd.to_datetime(df1["STARTING_DATE"])
df1["TODAY_DATE"]= pd.to_datetime(df1["TODAY_DATE"])
df1['SPENT_DAYS']=df1.TODAY_DATE-df1.STARTING_DATE
df1.SPENT_DAYS=df1.SPENT_DAYS.astype(str)
df1.SPENT_DAYS=df1.SPENT_DAYS.str.replace(' days','')
df1.JOB_DAYS=df1.JOB_DAYS.astype('int')
df1.reset_index(inplace=True)
df1.set_index('TEAM_NO.')
df1.SPENT_DAYS=df1.SPENT_DAYS.astype('int')+1
df1.SPENT_DAYS=df1.SPENT_DAYS.astype(str)+"/"+df1.JOB_DAYS.astype(str)
df1['STARTING_DATE']=df1['STARTING_DATE'].dt.strftime('%d-%m-%Y')
df1['TODAY_DATE']=df1['TODAY_DATE'].dt.strftime('%d-%m-%Y')
df1=df1.set_index('TEAM_NO.')
#df1['CRITICAL_CLOSURE_%']=df1['CRITICAL_CLOSURE_%'].astype(str)
#df1['CRITICAL_CLOSURE_%']=df1['CRITICAL_CLOSURE_%']+"%"
if Inv in df1["JOB_TYPE"].unique():
  Alert=1
  Invo=df1[df1["JOB_TYPE"]==Inv]
  df1.drop(df1[df1["JOB_TYPE"]==Inv].index, axis=0, inplace=True)

######################## df2 #############################################################
df2 = pd.read_excel(File,'Drops_Teams_Follow_Up')
df2.columns  = [i.replace(' ','_') for i in df2.columns]
df2.columns  = [i.upper() for i in df2.columns]
df2.dropna (axis=0, inplace=True)
df2['RIG_NO.']  = [i.replace(' ','') for i in df2['RIG_NO.']]
df2['RIG_NO.']  = [i.upper() for i in df2['RIG_NO.']]


df2['LAST_VISIT']=df2['LAST_VISIT'].astype(str)
df2['LAST_VISIT']=df2['LAST_VISIT'].str.split(' ').str[0]
df2["LAST_VISIT"]= pd.to_datetime(df2["LAST_VISIT"])
df2=df2.set_index('TEAM_NO.')
df2['TODAY_DATE']=datetime.date.today()
df2["TODAY_DATE"]= pd.to_datetime(df2["TODAY_DATE"])
df2['DAYS_COUNT'] = df2.TODAY_DATE-df2.LAST_VISIT
df2['LAST_VISIT']=df2['LAST_VISIT'].dt.strftime('%d-%m-%Y')
df2['DAYS_COUNT']=df2['DAYS_COUNT'].astype('str')
df2['DAYS_COUNT']=df2['DAYS_COUNT'].str.split(' ').str[0:2].str.join(' ')
df2.drop(['WELL_NAME','TODAY_DATE','FIELD'],axis=1, inplace=True)
######################## df3 #############################################################
df3 = pd.read_excel(File,'All_Critical_Points')
df3.columns  = [i.replace(' ','_') for i in df3.columns]
df3.columns  = [i.upper() for i in df3.columns]
df3.dropna(axis=0, inplace=True)

df3['RIG_NO.']  = [i.replace(' ','') for i in df3['RIG_NO.']]
df3['RIG_NO.']  = [i.upper() for i in df3['RIG_NO.']]
df3['PHASE']  = [i.replace(' ','') for i in df3['PHASE']]
df3['PHASE']  = [i.upper() for i in df3['PHASE']]


df3['FINAL_STATUS']=df3['FINAL_\nSTATUS'].str.upper()
df3.drop('FINAL_\nSTATUS',axis=1, inplace=True)
Rigs=df1['RIG_NO.'].unique()
Rigs=tuple(Rigs)



st.image(image)

 



st.markdown(" <center>  <h1> Daily Follow Up </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)




if Alert==1:
  col1, col2, col3 = st.columns(3)

  col1.write("    ")
  
  imm = Image.open("Alert.jpg")
  imagee = np.array(imm)
  col2.image(imagee)
  col3.write("    ")
  st.markdown('<center> <h1> <span style="color:red;"> Incident Investigation </span></h1> </font> </center> </h1>',unsafe_allow_html=True)
  Invo.drop(['TODAY_DATE','JOB_DAYS','index'], axis=1, inplace=True)
  Invo['SPENT_DAYS'] =Invo['SPENT_DAYS'].str.split('/').str[0] 
  Invo=Invo.transpose()
  
  st.dataframe(Invo,use_container_width=True) 




st.markdown(" <right>  <h1> (I) Survey/Audit</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
Audit=df1

Audit.drop(['TODAY_DATE','JOB_DAYS','index'], axis=1, inplace=True)
Audit=Audit.transpose()

st.dataframe(Audit)
st.write("Not mentioned audit teams are at home")
st.write("For more details you can check the plan")


st.markdown(" <right>  <h1> (II) Drops Survey </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)


Drops=df2
Drops=Drops.transpose()
st.dataframe(Drops)
st.write("Not mentioned drops teams are at home")
st.write("For more details you can check the plan")



st.markdown(" <center> <h1> Open Critical Items for Active Rigs </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



RB1=st.radio("Select an Active Rig: ",Rigs)

Team=df1
Team.reset_index(inplace=True)

for i in range(0,len(Rigs)):
            if RB1==Rigs[i]:
                        S=Team[Team['RIG_NO.']==Rigs[i]]['TEAM_NO.']
                        S=tuple(S)
                        st.write(f"Critical Points of Rig {Rigs[i]} ({S[0]}) ")
                        Critical = df3[df3['RIG_NO.']==Rigs[i]]
                        Critical.drop(['RIG_NO.','LOCATION','REF.','PRIORITY','RIG_TYPE'],axis=1,inplace=True)
                        Critical=Critical.set_index('NO.')
                        T1=st.dataframe(Critical,use_container_width=True)
                        J=len(list(df3[df3["RIG_NO."]==RB1]['PHASE']))
                        Rig_Phase=tuple((df1[df1['RIG_NO.']==RB1]['JOB_TYPE']).unique())
                        Rig_Phase=Rig_Phase[0]
                        JJ=len(list(df3[(df3["RIG_NO."]==RB1)&(df3["PHASE"]==Rig_Phase)]['PHASE']))
                        st.write(f"The total points of Rig {RB1}={J}")
                        st.write(f" Recent Points of {RB1} at {Rig_Phase} ={JJ} ")





# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




