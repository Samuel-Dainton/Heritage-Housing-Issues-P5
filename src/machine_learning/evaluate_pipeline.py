import streamlit as st
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error 
import numpy as np

def regression_performance(X_train, y_train, X_test, y_test,pipeline):
	st.write("Model Evaluation \n")
	st.write("* Train Set")
	st.code(regression_evaluation(X_train,y_train,pipeline))
	st.write("* Test Set")
	st.code(regression_evaluation(X_test,y_test,pipeline))

def regression_evaluation(X,y,pipeline):
  prediction = pipeline.predict(X)
  st.code('R2 Score:', r2_score(y, prediction).round(3))  
  st.code('Mean Absolute Error:', mean_absolute_error(y, prediction).round(3))  
  st.code('Mean Squared Error:', mean_squared_error(y, prediction).round(3))  
  st.code('Root Mean Squared Error:', np.sqrt(mean_squared_error(y, prediction)).round(3))

