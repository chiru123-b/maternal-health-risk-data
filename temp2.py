# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:21:42 2022

@author: chiranjeevi
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict(Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate):
    
       
  input_data=(25,130,80,15,98,86)
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=classifier.predict(input_data_reshaped)
  print(prediction)

  if(prediction[0]==0):
      return"High risk"
  elif(prediction[1]==1):
      return"Mid risk"
  else:
      return"Low risk"
     
 


def main():
    st.title("Maternal risk ")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit  Maternal risk web app  </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age=st.text_input('Age','Type here')
    SystolicBP=st.text_input('SystolicBP','Type here')
    DiastolicBP=st.text_input('DiastolicBP','Type here')
    BS=st.text_input('BS','Type here')
    BodyTemp=st.text_input('BodyTemp','Type here')
    HeartRate=st.text_input('HeartRate','Type here')
    
    result=""
    if st.button("Prediction"):
        result=predict(Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate)
    st.success(result)
    
    if(prediction[0]==0):
      return"High risk"
    elif(prediction[1]==1):
      return"Mid risk"
    else:
      return"Low risk"
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()