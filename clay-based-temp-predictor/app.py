import streamlit as st
import pickle
import pandas as pd
import numpy as np



pipe = pickle.load(open('BHT-Clay.pkl','rb'))
st.title('Clay Predictor')


LatDegree = st.number_input('LatDegree')
LongDegree = st.number_input('LongDegree')
ReportedElevation_m = st.number_input('ReportedElevation_m')
Clay = st.number_input('Clay')
MeasureDepth_m = st.number_input('MeasureDepth_m')


# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict Clay'):
      input=pd.DataFrame({'LatDegree':[LatDegree],'LongDegree':[LongDegree],'ReportedElevation_m':[ReportedElevation_m],'Clay':[Clay],'MeasureDepth_m':[MeasureDepth_m]})
      result = pipe.predict(input)
      st.success('THE Clay FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)