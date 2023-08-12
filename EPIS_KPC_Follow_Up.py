from PIL import Image
import streamlit as st
import numpy as np #1
import pandas as pd #2
import datetime
File="Client_EPIS_Daily_Progress.xlsx"
im = Image.open("EPIS.png")
image = np.array(im)



df1 = pd.read_excel(File,'Teams_Follow_Up')
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
df1["TEAM_NO."]  =  ["Team_"]+df1["TEAM_NO."].astype("str")+" ("+df1["AUDIT/DROPS"]+")"
df1.reset_index(inplace=True)
df1.set_index('TEAM_NO.')
df1.SPENT_DAYS=df1.SPENT_DAYS.astype('int')+1
df1.SPENT_DAYS=df1.SPENT_DAYS.astype(str)+"/"+df1.JOB_DAYS.astype(str)
df1['STARTING_DATE']=df1['STARTING_DATE'].dt.strftime('%d-%m-%Y')
df1['TODAY_DATE']=df1['TODAY_DATE'].dt.strftime('%d-%m-%Y')
df1=df1.set_index('RIG_NO.')


st.image(image)


st.markdown(" <center>  <h1> Daily Jobs on Active Rigs </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



st.markdown(" <right>  <h1> (I) Inspection/Audit Teams</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
Audit=df1[df1['AUDIT/DROPS']=="Audit"]
Audit.drop(['TODAY_DATE','JOB_DAYS','AUDIT/DROPS'], axis=1, inplace=True)
Audit=Audit.transpose()
#st.write(Audit)
st.dataframe(Audit.style.highlight_max(axis=0))



st.markdown(" <right> <h1> (II) The Car of the highest selected feature</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

RB1=st.radio("Select one of The Desired Feature: ",('TAX','PRICE','MILEAGE'))
if RB1=='TAX':
    O1=5
    st.write(O1)



st.markdown(" <center>  <h1> B) Data Average Values </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



Tog1 = st.selectbox("Desired Model Selection ",(' A1', ' A6', ' A4', ' A3' ,' Q3', ' Q5', ' A5' ,' S4', ' Q2', ' A7', ' TT', ' Q7',' RS6' ,' RS3', ' A8' ,' Q8' ,' RS4', ' RS5' ,' R8', ' SQ5', ' S8', ' SQ7', ' S3',' S5' ,' A2', ' RS7'))

Y=st.slider('Select the year you are interested in',1997,2020)

#O3=data[(data['MODEL']==Tog1) & (data['YEAR']==Y) ].mean(axis=0)['TAX']
O3=4
st.write(f'The Average Taxes for the model {Tog1} ',O3,'Euro')

# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




