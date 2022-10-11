# Heritage Housing Issues
* A data analytics project to clean and engineer data for an ML Model that predicts the value of a house in Ames, Iowa and to help visualize the most important features considered when predicting that value.



## Business Requirements
You are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in their own state and residential area, they fear that basing their estimates for property worth on their current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where they come from might not be the same in Ames, Iowa. They found a public dataset with house prices for Ames, Iowa, and will provide you with that

* 1 - The client is interested in discovering how house attributes correlate with the typical house Sale Price. Therefore, the client expects data visualizations of the correlated variables against Sale Price to show that.
    * For this we will need to present the data in a way that is easy to understand, showcasing the major variables that affect a house's sale price.
* 2 - The client is interested in predicting the house sales price from their 4 inherited houses, and any other house in Ames, Iowa.
    * We will need to create a dashboard where the user can enter the key variables of their houses in order to give them a price estimate.

---

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created a fictitious user story where predictive analytics could be applied to a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

---

## Epics and User Stories

| User | User wants to be able to.. | So they can..    |
| :---:   | :---: | :---: |
| Client | Navigate dashboard pages easily   | Easily absorb all information presented by the dashboard   |
| | View features that correlate with house sale price | Gain an understanding of what factors increase a houses sale price |
| | Input house key variables into a sales price prediction app | Estimate the value of their houses |
| Data Scientist | View a breakdown of the ML pipelines | Have an understanding of how the data is prepared and used in predicting sale price |

Most user stories all fall into the epic category of dashboard planning, design and development.

![Canban](/media/canban.png)

---

## Hypothesis and how to validate?
* 1 - We suspect houses with larger square footing may have had a higher sales price.
	* A Correlation study can help in this investigation
* 2 - We suspect that between houses with similar square footing, those with a more recent Year Built date may have had a higher sales price.
	* A Correlation study can help in this investigation
* 3 - We suspect that between houses with similar square footing and year built date, those with a more recent Remodel date may have had a higher sales price.
	* A Correlation study can help in this investigation
* 4 - We suspect that between houses with similar square footing, those with higher quality and condition scores may have had a higher sales price.
	* A Correlation study can help in this investigation

---

## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation study
	* We will inspect the data related to the houses.
	* We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price.
	* We will plot the main variables against Sale Price to visualize insights.

* **Business Requirement 2:** Regression, Data Analysis
	* We want to predict the value of a house. We want to build a regression model to predict the dependent variable.
	* We want to make plots to visualize the train and test sets predictions vs the actual.
	* We want to run regression evaluation to demonstrate the R2 Score and Mean Absolute Error.

---

## ML Business Case

### Predict Sale Price
#### Regression Model

* We want an ML model to predict the sale price of a house. A target variable is a continuous number. We consider a **regression model**, which is supervised and uni-dimensional.
* Our ideal outcome is to provide our client with reliable insight into what sale price they should expect for their inherited houses.
* The model success metrics are
	* At least 0.7 for R2 score, on train and test set
	* The ML model is considered a failure if:
		* after 12 months of usage, the model's predictions are 50% off more than 30% of the time. Say, a prediction is >50% off if predicted 10 months and the actual value was 2 months.
* The output should be a continuous value for sale price. 

### Data Decision Making
* On a few occasions I was questioned for using the ArbitraryNumberImputer for filling the missing data of `2ndFlrSf, EnclosedPorch, MasVnrArea and WoodDeckSF` instead of MeanMedianImputer. My reasoning for this was that in all of these variables the Mode value is 0. `EnclosedPorch` for example has 90% of it's data missing. And of the 10% remaining, 8% of it is zeroes. This is similar for all variables relating to area or size of features, which suggests that in the data collection these fields were often left blank instead of filling them with 0 when a house simply did not have a 2nd floor, wood deck or other feature.

* I wanted to fill the missing values for `GarageYrBlt` with the same values as `YearBuilt` due the two almost always sharing the same date or the Garage Built date being just one or two years after. However, I ran into an error that I wasn't able to move past, the method I used to `fillna` the empty values in my pipeline was at some point causing a ValueError when put though the hyperparameter optimization search. I wasn't able to fix this as so opted to use the MeanMedianImputer instead. This would lead to some odd data, like houses having garages built before the house, but ultimately wouldn't cause much of an impact to the model.

* Lastly, I wanted to use the OutlierTrimmer instead of the Windsorizer on `SalePrice, GrLivArea and TotalArea`. To do so however would require me to make a number of changes to the order of the pipeline. Currently the train and test sets are split and then have the cleaning and engineering steps applied to them in the pipeline. The problem with this, is that by splitting the sets and then trimming them of outliers, the sets always end up with imbalanced amounts of data and cause the pipeline to get stuck. 

---

## Dashboard Design

### Page 1: Quick project summary
* Quick project summary
	* Project Terms & Jargon
	* Describe Project Dataset
	* State Business Requirements

### Page 2: House Sale Price Study
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1
	* Checkbox: data inspection on house sale data (display the number of rows and columns in the data, and display the first ten rows of the data)
	* Display the most correlated variables to house price and the conclusions
	* Checkbox: Individual plots showing the house price levels for each correlated variable 
	* Checkbox: Plot that shows house prices and correlated variables with a hue of OverallQuality

### Page 3: House Value Estimator
* State business requirement 2
* Set of widgets inputs, which relate to the house variables. Each set of inputs is related to a given ML task to predict a houses SalePrice.
* "Run predictive analysis" button that serves the input data to our ML pipelines, and predicts the value of the house.

### Page 4: Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
* 1 - We suspect houses with larger square footing may have had a higher sales price.

	* Correct. There is strong correlation between the two. The correlation study on the House Sale Price Study supports this hypothesis.

* 2 - We suspect that between houses with similar square footing, those with a more recent Year Built date may have had a higher sales price.

	* Correct. There is moderate correlation between the two. The correlation study on the House Sale Price Study supports this. It's worth noting that houses with a more recent Year Built date are typically higher in Overall Quality which has much stronger correlationto Sale Price.

* 3 - We suspect that between houses with similar square footing and year built date, those with a more recent Remodel date may have had a higher sales price.

	* Correct. There is weak to moderate correlation between the two. Again, it is worth noting that there is a relationship between houses with a more recent Remodel date being higher in Overall Quality

* 4 - We suspect that between houses with similar square footing, those with higher quality and condition scores may have had a higher sales price.

	* Correct. There is strong correlation between the two variables.The correlation study on the House Sale Price Study supports this hypothesis.

### Page 5: ML: Predict House Value
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

---

## Unfixed Bugs
* There is one unsolved bug in page 5 of the app, related to the evaluate_pipeline.py file, where for some reason in the app on the last page, the function always outputs an extra line of 'None'. I've spent a great deal of my tutors time and my own searching for why this might be but haven't come across a reason for it.

---

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

---

## Main Data Analysis and Machine Learning Libraries

* Matplotlib - Creates various graphs and plots to visualize the data. 
* Seaborn - For visualizing the data in the Streamlit app with plots, graphs and more.
* ppscore - Used to study the power predictive score of variables against one another.
* Streamlit - Creating the app to present the study.
* Feature-Engine - Major library for engineering the data for the pipeline.
* Scikit-Learn - Creating the pipeline and applying various algorithms, feature engineering steps and more to it.
* Numpy - To process arrays that store values, aka data. It facilitates math operations and their vectorization.
* Pandas and Pandas-Profiling - For data analysis, data exploration, data manipulation, data visualization.

---

## Credits 
### Content 

- The template for this project was created by Code Institute
- A number of functions were built for this project by Code Institute and are credited throughout the notebooks.
- The dataset is provided by [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)
- All learning material was sourced through either the Code Institute program or the documentation of the various libraries used.

---

## Acknowledgements
* A big thank you to Niel McEwen of Code Institute who is quick and eager to help with the many questions I had during my studies.

