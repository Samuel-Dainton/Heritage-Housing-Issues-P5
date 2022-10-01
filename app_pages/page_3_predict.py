import streamlit as st
import streamlit as st
import pandas as pd
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_sale_price)

def page_3_predict_body():

	# load predict sale_price files
	version = 'v1'
	sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
	sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
					.columns
					.to_list()
					)


	st.write("### Predict House Sale Price")

	st.info(
        f"* 2 - The client is interested to predict the house sale price for their 4 "
        f"inherited houses, and any other house in Ames, Iowa. "
	)

	st.write("---")

	
	# Generate Live Data
	# check_variables_for_UI(sale_price_features)
	X_live = DrawInputsWidgets()


	# predict on live data
	if st.button("Run Predictive Analysis"): 
		predict_sale_price(X_live, sale_price_features, sale_price_pipe)

			



def check_variables_for_UI(sale_price_features):
	import itertools

	# The widgets inputs are the features used in all pipelines (sale_price)
	# We combine them only with unique values
	combined_features = set(
		list(
			itertools.chain(sale_price_features)
			)
		)
	st.write(f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")



def DrawInputsWidgets():

	# load dataset
	df = load_house_data()
	percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets for 6 features or more	
	col1, col2, col3, col4 = st.beta_columns(4)
	col5, col6, col7, col8 = st.beta_columns(4)

	# We are using these features to feed the ML pipeline
		
	# create an empty DataFrame, which will be the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# from here on we draw the widget based on the variable type (numerical or categorical)
	# and set initial values

	with col1:
		feature = "OverallQual"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col3:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col4:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget

	with col6:
		feature = "YearRemodAdd"
		st_widget = st.number_input(
			label= feature,
			min_value= df[feature].min()*percentageMin,
			max_value= df[feature].max()*percentageMax,
			value= df[feature].median()
			)
	X_live[feature] = st_widget


	# st.write(X_live)

	return X_live
