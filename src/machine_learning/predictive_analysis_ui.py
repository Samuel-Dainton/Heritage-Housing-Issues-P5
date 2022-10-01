import streamlit as st

def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_sale_price = X_live.filter(sale_price_features)

	# predict
	sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)
	sale_price_prediction_proba = sale_price_pipeline.predict(X_live_sale_price)
	# st.write(sale_price_prediction_proba)

	# create a logic to display the results
	proba = sale_price_prediction_proba[0,sale_price_prediction][0]*100

	if sale_price_prediction != 1:
		statement = (
			f"* In addition, there is a {proba.round(2)}% probability the prospect "
			f"will stay **{sale_price_levels} months**. "
			)
	else:
		statement = (
			f"* The model has predicted the prospect would stay **{sale_price_levels} months**, "
			f"however we acknowledge that the recall and precision levels for {sale_price_levels} is not "
			f"strong. The AI tends to identify potential churners, but for this prospect the AI is not "
			f"confident enough on how long the prospect would stay."
		)
		
	st.write(statement)