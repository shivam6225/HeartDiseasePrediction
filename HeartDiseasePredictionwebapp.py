# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:01:29 2022

@author: LENOVO
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('D:/shiva/downloads/heart_disease_model.sav','rb'))

with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction',
                           'Information on Heart Disease'
                          ],
                          icons=['heart','info-circle'],
                          default_index=1)
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    heart_diagnosis = ''
   
    if st.button('Heart Disease Test Result'):
        a=[[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]]
        b=np.array(a, dtype=float)
        heart_prediction = heart_disease_model.predict(b)                          
       
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
       
    st.success(heart_diagnosis)
        
        
if (selected == 'Information on Heart Disease'):
    st.title('Heart Disease')
    
    st.markdown('The term “heart disease” refers to several types of heart conditions. The most common type of heart disease is coronary artery disease (CAD), which affects the blood flow to the heart. Decreased blood flow can cause a heart attack.')
    st.subheader('Symptoms of Heart Disease')    
    st.markdown('Sometimes heart disease may be “silent” and not diagnosed until a person experiences signs or symptoms of a heart attack, heart failure, or an arrhythmia. When these events happen, symptoms may include:')
    st.markdown('* Heart attack: Chest pain or discomfort, upper back or neck pain, indigestion, heartburn, nausea or vomiting, extreme fatigue, upper body discomfort, dizziness, and shortness of breath.')
    st.markdown('* Arrhythmia: Fluttering feelings in the chest (palpitations). ')
    st.markdown('* Heart failure: Shortness of breath, fatigue, or swelling of the feet, ankles, legs, abdomen, or neck veins.')
    st.subheader('Risk Factor for Heart Disease')
    st.markdown('* Diabetes')
    st.markdown('* Overweight and obesity')
    st.markdown('* Unhealthy diet')
    st.markdown('* Physical inactivity')
    st.markdown('* Excessive alcohol use')
