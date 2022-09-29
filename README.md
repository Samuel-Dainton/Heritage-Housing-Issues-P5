## Business Requirements
You are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in their own state and residential area, they fear that basing their estimates for property worth on their current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where they come from might not be the same in Ames, Iowa. They found a public dataset with house prices for Ames, Iowa, and will provide you with that

* 1 - The client is interested in discovering how house attributes correlate with the typical house Sale Price. Therefore, the client expects data visualizations of the correlated variables against Sale Price to show that.
    * For this we will need to present the data in a way that is easy to understand, shocasing the major variables that effect a houses sales price.
* 2 - The client is interested to predict the house sales price from their 4 inherited houses, and any other house in Ames, Iowa.
    * We will need to create a dashboard where the user can enter the key variables of their houses in order to give them a price estimate.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created a fictitious user story where predictive analytics could be applied to a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
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

## Epics and User Stories

| User | User wants to be able to.. | So they can..    |
| :---:   | :---: | :---: |
| Client | Navigate dashboard pages easily   | Easily absorb all information presented by the dashboard   |
| | View features that correlate with house sale price | Gain an understanding of what factors increase a houses sale price |
| | Input house key variables into a sales price prediction app | Estimate the value of their houses |
| Data Scientist | View a breakdown of the ML pipelines | Have an understanding of how the data is prepared and used in predicting sale price |

Most user stories all fall into the epic catagory of dashboard planning, design and development.

![Canban](/media/canban.png)

## Hypothesis and how to validate?
* 1 - We suspect houses with larger square footing may have had a higher sales price.
	* A Correlation study can help in this investigation
* 2 - We suspect that between houses with similar square footing, those with a more recent Year Built date may have had a higher sales price.
	* A Correlation study can help in this investigation
* 3 - We suspect that between houses with similar square footing and year built date, those with a more recent Remodel date may have had a higher sales price.
	* A Correlation study can help in this investigation
* 4 - We suspect that between houses with similar square footing, those with higher quality and condition scores may have had a higher sales price.
	* A Correlation study can help in this investigation


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation study
	* We will inspect the data related to the houses.
	* We will conduct a correlation study (Pearson and Spearman) to understand better how the variables are correlated to Sale Price.
	* We will plot the main variables against Sale Price to visualize insights.

* **Business Requirement 2:** Regression, Cluster, Data Analysis
	* We want to predict the value of a house. We want to build a regression model to predict the dependant variable.
	* We want to cluster similar houses, to predict which cluster a prospect will belong in.
	* We want to understand a cluster profile which could present potential options to remodel a house and bring the prospect to a cluster that typically yields a higher sales price.


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
	* Correct. The correlation study on the House Sale Price Study supports this hypothesis.
* 2 - We suspect that between houses with similar square footing, those with a more recent Year Built date may have had a higher sales price.
	* Incorrect. There is only small correlation between the two. The correlation study on the House Sale Price Study supports this.
* 3 - We suspect that between houses with similar square footing and year built date, those with a more recent Remodel date may have had a higher sales price.
	* Incorrect. This showed even less of a correlation than our hypothesis on YearBuilt. 
* 4 - We suspect that between houses with similar square footing, those with higher quality and condition scores may have had a higher sales price.
	* Correct. The correlation study on the House Sale Price Study supports this hypothesis.

### Page 5: ML: Predict House Value
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

