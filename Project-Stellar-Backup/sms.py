import streamlit as st
from twilio.rest import Client
import pandas as pd
import numpy as np


def smsDriver(client):
    df=""
    st.title("For SMS")
    st.markdown("### Upload a CSV File for SMS")
    file=st.file_uploader("",key="sms")
    send=None
    if(not file):
        st.warning("Upload the number files")
    else:
        df=pd.read_csv(file)
        st.markdown("Detected **"+ str(len(df))+"** Mobile Numbers")
        number=df["num"].tolist()
        message=st.text_input("Enter your Text message")
        send=st.button("Send the message")
        #st.write(number)
    if(send):
        try:
            for n in number:
                client.messages.create(to=n,from_="+19032895538",body=message)
            st.success("Message sending successfull")
            st.info("It might take some time to recieve the message")
        except Exception as e:
            st.error("Got Error: "+str(e))