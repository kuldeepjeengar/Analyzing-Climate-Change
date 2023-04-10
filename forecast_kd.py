import streamlit as st
import pandas as pd
import pickle

# load the saved model from the .sav file
with open('Final_for.sav', 'rb') as file:
    model = pickle.load(file)
    
    
predictions=[]
predictions=model.forecast(steps=482)
predictions.append(predictions)
pred=predictions.reset_index()
forecasting=pd.DataFrame.rename(pred,columns={"index":"year","predicted_mean":"avg_temprature"})
forcast=forecasting.set_index("year")

# function to get the temperature prediction for a given year
def predict_temperature(year):
    # create a DataFrame with the input year as a single row
    #input_data = pd.DataFrame({'year': [year]})
    
    st.write(forcast['avg_temprature'][year])
    # use the model to make a single prediction for the input year
    #prediction = model.forecast(steps=1, exog=input_data)

    # return the predicted temperature as a float
    return

# create a Streamlit app
st.title('Temperature Prediction')
year = st.slider('Enter a year:', min_value=2000, max_value=2482, step=1)
if st.button('Predict'):
    predict_temperature(year)
    
  #st.write('The predicted temperature for {year} is' : {temperature:.1f} degrees.')
    
    
    