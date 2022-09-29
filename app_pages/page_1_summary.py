import streamlit as st

def page_1_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* **SalePrice** is the price a house is sold for and is our target variable.\n"
        f"* There are many abreviated terms used to describe features of the houses in"
        f"* the data set. In this app we will expand on all of them but for further"
        f"* clarification the full dataset and explination of it's terms can be found [here](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n\n"
        f"**Project Dataset**\n"
        f"* The dataset has almost 1.5 thousand rows of data and represents housing records from "
        f"Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses "
        f"built between 1872 and 2010. "
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and read the "
        f"[Project README file](https://github.com/Samuel-Dainton/Heritage-Housing-Issues-P5).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how house attributes correlate with "
        f"the typical house Sale Price. Therefore, the client expects data visualizations "
        f"of the correlated variables against Sale Price to show that.\n"
        f"* 2 - The client is interested to predict the house sales price from their 4 "
        f"inherited houses, and any other house in Ames, Iowa. "
        )
