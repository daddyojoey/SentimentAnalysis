!pip install joblib
import streamlit as st
import joblib
#load the trained model
model= joblib.load("sentiment-model.pkl")
#Define sentiment labels
sentiment_labels = {'1': 'positive' , '0': 'negative'}

#create Streamlit app
st.title("Sentiment Analysis")

#Input text area

user_input =st.text_area("Enter your texxt here")

#Prediction button

if st.button("Predict"):
    #perform sentiment prediction
    print(user_input)
    Predicted_sentiment = model.predict([user_input])[0]
    print("predicted_sentiment_label = sentiment_labels:"+str(Predicted_sentiment))
    predicted_sentiment_label = sentiment_labels[str(Predicted_sentiment)]

    #Display predicted sentlement
    st.info(f"Predicted Sentiment : {predicted_sentiment_label}")
