import streamlit as st

def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(sale_price_features)

	# predict
	sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)
	# st.write(sale_price_prediction_proba)

	# create a logic to display the results
	proba = sale_price_prediction_proba

		
	st.write(proba)