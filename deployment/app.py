# model deployment using all in one method

import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Milestone 2",
    page_icon= "🍂" ,
    layout="centered", 
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Country Happiness Score"
    }
)

with open("final_pipe.pkl", "rb") as model_file:
    model = pickle.load(model_file)

columns=['Region', 'GDP', 'Social_support', 'Healthy', 'Freedom', 'Generosity', 'Corruption']

st.markdown("<h1 style='text-align: center; color: black;'>Country Happiness Score</h1>", unsafe_allow_html=True)
left_column, right_column = st.columns(2)
with left_column:
    Region = st.selectbox("Region", ['Western Europe', 'Latin America and Caribbean',
                                'Middle East and Northern Africa', 'Southeastern Asia',
                                'Eastern Asia', 'Central and Eastern Europe', 'Sub-Saharan Africa',
                                'Southern Asia', 'Australia and New Zealand', 'North America'])
    st.caption('Region is an area of a country or any part of the world having common features.')
with right_column:
    GDP = st.number_input("Log GDP per capita")
    st.caption('GDP per capita is in terms of Purchasing Power Parity (PPP) adjusted to constant 2011 international dollars, taken from the World Development Indicators (WDI) released by the World Bank on November 14, 2018.')
st.caption('---')

left_column, right_column = st.columns(2)
with left_column:
    Social_support = st.number_input("Social support")
    st.caption('Social support is the national average of the binary responses (either 0 or 1) to the Gallup World Poll (GWP) question “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”')
with right_column:
    Healthy = st.number_input("Healthy life expectancy at birth")
    st.caption('The time series of healthy life expectancy at birth are constructed based on data from the World Health Organization (WHO) Global Health Observatory data repository, with data available for 2005, 2010, 2015, and 2016. ')
st.caption('---')

left_column, right_column = st.columns(2)
with left_column:
    Freedom = st.number_input("Freedom to make life choices")
    st.caption('Freedom to make life choices is the national average of binary responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”')
with right_column:
    Generosity = st.number_input("Generosity")
    st.caption('Generosity is the residual of regressing the national average of GWP responses to the question “Have you donated money to a charity in the past month?” on GDP per capita.')
st.caption('---')

left_column, right_column = st.columns(2)
with left_column:
    Corruption = st.number_input("Perceptions of corruption")
    st.caption('Perceptions of corruption are the average of binary answers to two GWP questions: “Is corruption widespread throughout the government or not?” and “Is corruption widespread within businesses or not?” Where data for government corruption are missing, the perception of business corruption is used as the overall corruption-perception measure.')


# Data Inference
new_data = [Region, GDP, Social_support, Healthy, Freedom, Generosity, Corruption]
new_data = pd.DataFrame([new_data], columns=columns)
pred = model.predict(new_data)

button = st.button("Predict")

if button:
    st.write('The predicted happiness score is: ')
    st.subheader(pred[0])

    if pred > 5.51:
        st.write('The country happiness score is higher than 5.51, then the country is more happy than the average country in the world.')
    else:
        st.write('The country happiness score is lower than 5.51, then the country is less happy than the average country in the world.')