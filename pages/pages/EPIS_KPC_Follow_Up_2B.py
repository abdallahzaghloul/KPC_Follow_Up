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
df1['TODAY_DATE']=datetime.date.today()
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
df1['CRITICAL_CLOSURE_%']=df1['CRITICAL_CLOSURE_%'].astype(str)
df1['CRITICAL_CLOSURE_%']=df1['CRITICAL_CLOSURE_%']+"%"
######################## df3 #############################################################
df3 = pd.read_excel(File,'Active_Critical_Points')
df3.columns  = [i.replace(' ','_') for i in df3.columns]
df3.columns  = [i.upper() for i in df3.columns]
df3.dropna(axis=0, inplace=True)
df3['FINAL_STATUS']=df3['FINAL_\nSTATUS'].str.upper()
df3.drop('FINAL_\nSTATUS',axis=1, inplace=True)
Rigs=df3['RIG_NO.'].unique()
Rigs=tuple(Rigs)
st.image(image)


st.markdown(" <center>  <h1> Daily Follow Up </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



st.markdown(" <right>  <h1> (I) Survey/Audit</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
Audit=df1

Audit.drop(['TODAY_DATE','JOB_DAYS','index'], axis=1, inplace=True)
Audit=Audit.transpose()

st.dataframe(Audit)


st.markdown(" <right>  <h1> (II) Drops Survey </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)



#Drops=df2
#Drops.drop(['TODAY_DATE','JOB_DAYS','index'], axis=1, inplace=True)
#Drops=Drops.transpose()
st.write("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#st.dataframe(Drops.style.highlight_max(axis=0))



st.markdown(" <center> <h1> Open Critical Items for Active Rigs </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



RB1=st.radio("Select an Active Rig: ",Rigs)

Team=df1.reset_index(inplace=True)
for i in range(0,len(Rigs)):
            if RB1==Rigs[i]:
                        st.write(f"Critical Points of Rig {Rigs[i]} {(Team[Team['RIG_NO.']==Rigs[i]]['TEAM_NO.'][0])} ")
                        Critical = df3[df3['RIG_NO.']==Rigs[i]]
                        Critical.drop(['RIG_NO.','LOCATION','REF.','PRIORITY'],axis=1,inplace=True)
                        Critical=Critical.set_index('NO.')
                        T1=st.dataframe(Critical,use_container_width=True)                                    




# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




