

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_pipeline import regression_performance, regression_evaluation_plots


def page_5_ml_predict_body():

    st.write("### ML: Predict House Value")

    # load tenure pipeline files
    version = 'v1'
    best_regressor_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
    sale_price_features = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    # display pipeline training summary conclusions
    st.info(
        f"* We wanted to have a Regressor model to predict Sale Price for houses. "
        f"We managed to reach above our target R2 score of 0.7 and did attempt to "
        f"imrove this score further by using a Regressor model with PCA but to no success. \n "
        f"A number of steps were taken to clean and engineer the data for the pipeline, "
        f"the highest performing steps and hyperparameters on the most important features "
        f"are listed below. "
    )

    st.write("---")

    # show pipeline steps
    st.write("* ML pipeline to predict Sale Price")
    st.code(best_regressor_pipeline)
    st.write("---")

    # show best features
    st.write("* The features the model was trained on and their importance")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # evaluate performance on both sets
    
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=best_regressor_pipeline)

    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=best_regressor_pipeline)   