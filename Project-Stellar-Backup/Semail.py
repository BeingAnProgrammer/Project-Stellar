import smtplib
#import logging
import pandas as pd
import numpy as np
import math #for ceil
import streamlit as st

sender=""#007senderemail@gmail.com")
password=""#pyoneers25"

def is_connected(con):
    try:
        status = con.noop()[0]
    except: 
        status = -1
    return True if status == 250 else False

def split_(df):
    dfList=list()
    size=0;n=len(df)
    if(len(df)>500):
        size=math.ceil(n/500)
        dfList=np.array_split(df, size)
    else:
        dfList=np.array_split(df,1)
    return dfList

def main(dfList,sender,password,body):
    #st.write("1: body: "+body)
    for data in dfList:
                #initiating instance
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        st.info("Started sending the email ") 
        #st.write("2: body: "+body) 
        for e in data.email:
            try:
                server.sendmail(sender, e, body)
                #st.write("3: body: "+body)
                #lg.info("Sending mail to "+e)
                st.write(e)
            except Exception as e:
                #lg.error(e)
                if( not is_connected(server)):
                    return
                else:
                    continue
        server.quit()
        

def emailDriver():
    st.title("Emailing System")

    sender=st.sidebar.selectbox("Enter the email to use",["007senderemail@gmail.com"])
    password =st.sidebar.text_input("Enter the password",type="password")#pegfmatnhrbomcxd
    subject = st.sidebar.text_input("Enter the Message Subject")#"Bulk message Test"
    msg = st.sidebar.text_input("Enter the Message to deliver")#"Hello this is a email form python"
    body = "Subject: {}\n\n{}".format(subject,msg)

    st.write("Upload a csv in <First name,Last Name,Number,Email>")
    st.markdown("### Upload a CSV File for SMS")
    file=st.file_uploader("",key="email")
    if(file):
        df=pd.read_csv(file)
        dfList=split_(df)
        st.markdown("Detected **"+ str(len(dfList[0]))+"** emails")
        send=st.button("Send the mail")
        if(send):
            st.write("aftr send body:"+body)
            main(dfList,sender,password,body)
            st.success("Email Sent")

        