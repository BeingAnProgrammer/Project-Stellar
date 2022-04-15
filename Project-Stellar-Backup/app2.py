import streamlit as st
from twilio.rest import Client
import pandas as pd
import numpy as np
from Semail import * #custom package
from sms import *

sms_client=Client("AC1b858528d369277efd22ff7f64d60ab0","952022611a0248835caf095c67e7c11d")

emailDriver()
st.markdown("---")
smsDriver(sms_client)