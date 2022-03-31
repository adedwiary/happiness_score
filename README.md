# Happiness Score Prediction
***
* Created 5 prediction model (Linear regression, Ridge Regression, Lasso Regression, K-Neighbors Regression, and XG Boost Regression) to predict country’s happiness score.
* Managed to receive a validation accuracy of over 92%.
* Used the World Happiness Report dataset.

## The World Happiness Report dataset.
The data consists of 1084 rows and 11 columns. with the following labels:

* **Country:** Name of the country.
* **Region:** Region is region the country belongs to.
* **GDP per capita:** GDP per capita is in terms of Purchasing Power Parity (PPP) adjusted to constant 2011 international dollars, taken from the World Development Indicators (WDI) released by the World Bank on November 14, 2018.
* **Healthy Life Expectancy:** The time series of healthy life expectancy at birth are constructed based on data from the World Health Organization (WHO) Global Health Observatory data repository, with data available for 2005, 2010, 2015, and 2016. 
* **Social support:** the national average of the binary responses (either 0 or 1) to the Gallup World Poll (GWP) question “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”
* **Freedom to make life choices:** the national average of binary responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”
* **Generosity:** the residual of regressing the national average of GWP responses to the question “Have you donated money to a charity in the past month?” on GDP per capita.
* **Perceptions of corruption:** the average of binary answers to two GWP questions: “Is corruption widespread throughout the government or not?” and “Is corruption widespread within businesses or not?” Where data for government corruption are missing, the perception of business corruption is used as the overall corruption-perception measure.

# Code and Resources used
***
* **Tool:** Visual Studio Code, Google Colaboratory
* **Packages:** Pandas, Scikit-learn, Matplotlib, Seaborn
* **World Happiness Report dataset** : https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021. 


# Findings
* 5 prediction model (Linear regression, Ridge Regression, Lasso Regression, K-Neighbors Regression, and XG Boost Regression) to predict country’s happiness score.
* The best model is the XG Boost Regression model with parameter learning_rate 0.1, and n_estimators 200 because it has the largest R-squared and the smallest MAE and RMSE compared to other models.
* Managed to obtain an accuracy close to 81%.

![model_evaluation](https://user-images.githubusercontent.com/97724828/161030627-7ec64aee-dc73-459d-87c6-1a4d3e506e7f.png)
\
The image above shows the model evaluation of the test datasets.
