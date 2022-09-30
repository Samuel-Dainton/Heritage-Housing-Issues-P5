import streamlit as st

import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

import numpy as np
import plotly.express as px


def page_2_sale_price_study_body():

    
    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Value Estimator")
    st.info(
        f"* The client is interested in understanding the patterns from the house sales data set, "
        f"so that they can learn what the most relevant variables correlated to SalePrice are."
    )

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"printed below are the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to SalePrice. \n"
        f"Some of the most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation tests in the notebook and the plots below"
        f"give the following indications: \n"
        f"* The SalePrice of a house is typically higher for a house with a larger Ground Living Area \n"
        f"* The SalePrice of a house is typically higher for a house with a higher Overall Quality  \n"
        f"* The SalePrice of a house is typically higher for a house with a more recent Year Built. "
        f"* this is due to houses with a more recent Year Built typically being higher in Overall Quality. \n"
        f"* Houses with larger sized features such as 1stFlrSF, GarageArea, TotalBsmtSF etc."
        f"* typically have a larger Ground Living Area. \n"
    )


    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(f"* Information in yellow indicates the profile from a churned customer")
        parallel_plot()

    
# function created using "02 - Churned Customer Study" notebook code - Parallel Plot section
def parallel_plot():
    df = load_house_data()
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.set_style("darkgrid")
    sns.lmplot(data=df, x="OverallQual", y="SalePrice", ci=None)
    st.pyplot(fig)
