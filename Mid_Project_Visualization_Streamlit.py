from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
Excel_Name="Client_EPIS_Daily_Progress.xlsx"
data=pd.read_csv(Excel_Name)

def Data_Columns_Uniting (data):
    data.columns = data.columns.str.upper().str.strip()
    data.columns = data.columns.str.replace(' ', '_')

Data_Columns_Uniting(data)

st.markdown(" <center>  <h1> Used Car Dataset Analysis </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)

im = Image.open("audi-logo-2016.png")
image = np.array(im)
st.image(image)


st.markdown(" <center>  <h1> A) Data Absolute Values </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)


data['KPL']=data['MPG'].apply(lambda x: x*0.425144)

data['KILOMETERSAGE']=data['MILEAGE'].apply(lambda x: x*19.10)





st.markdown(" <right>  <h1> (I) The Car of the lowest selected feature</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

RB2=st.radio("Select The Desired Feature: ",('TAX','PRICE','MILEAGE'))
if RB2=='TAX':
    O2=data[data['TAX']==data['TAX'].min()] #### The Model That has the lowest Mile Age
    st.write(O2)

elif RB2 == 'PRICE':
   O2=data[data['PRICE']==data['PRICE'].min()]   #### The Model That has the highest Mile Age
   st.write(O2)
   
elif RB2 == 'MILEAGE':
   O2=data[data['MILEAGE']==data['MILEAGE'].min()] #### The Model That has the lowest Mile Age
   st.write(O2)


st.markdown(" <right> <h1> (II) The Car of the highest selected feature</h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

RB1=st.radio("Select one of The Desired Feature: ",('TAX','PRICE','MILEAGE'))
if RB1=='TAX':
    O1=data[data['TAX']==data['TAX'].max()]   #### The Model That has the highest Mile Age
    st.write(O1)

elif RB1 == 'PRICE':
   O1=data[data['PRICE']==data['PRICE'].max()]   #### The Model That has the highest Mile Age
   st.write(O1)
elif RB1 == 'MILEAGE':
   O1=data[data['MILEAGE']==data['MILEAGE'].max()]   #### The Model That has the highest Mile Age
   st.write(O1)



st.markdown(" <center>  <h1> B) Data Average Values </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)



Tog1 = st.selectbox("Desired Model Selection ",(' A1', ' A6', ' A4', ' A3' ,' Q3', ' Q5', ' A5' ,' S4', ' Q2', ' A7', ' TT', ' Q7',' RS6' ,' RS3', ' A8' ,' Q8' ,' RS4', ' RS5' ,' R8', ' SQ5', ' S8', ' SQ7', ' S3',' S5' ,' A2', ' RS7'))

Y=st.slider('Select the year you are interested in',1997,2020)

O3=data[(data['MODEL']==Tog1) & (data['YEAR']==Y) ].mean(axis=0)['TAX']
O4=data[(data['MODEL']==Tog1)& (data['YEAR']==Y)].mean(axis=0)['PRICE']
O5=data[(data['MODEL']==Tog1)& (data['YEAR']==Y)].mean(axis=0)['MILEAGE']
O6=data[(data['MODEL']==Tog1)& (data['YEAR']==Y)].mean(axis=0)['ENGINESIZE']

st.write(f'The Average Taxes for the model {Tog1} ',O3,'Euro')
st.write(f'The Average Price for the model {Tog1} ',O4,'Euro')
st.write(f'The Average Mileage for the model {Tog1} ',O5,'Miles')
st.write(f'The Average ENGINESIZE for the model {Tog1} ',O6)


# streamlit run "C:\\Users\\hp\\Desktop\\Data Science\\Mid-Project\\Data_Visulaization_Project_Files\\Mid_Project_Visualization_Streamlit.py"




