import streamlit as st
import numpy as np
import random
import pandas as pd

email_data_list = [
    {
        "Company": "Facebook",
        "Date": "7/30",
        "Summary": "No",
        "Status": "Determination"
    },
    {
        "Company": "Amazon",
        "Date": "8/23",
        "Summary": "No",
        "Status": "Determination"
    },
    {
        "Company": "Apple",
        "Date": "9/4",
        "Summary": "Received",
        "Status": "Awaiting"
    },
    {
        "Company": "Netflix",
        "Date": "10/14",
        "Summary": "Yes",
        "Status": "Interview Scheduled"
    },
    {
        "Company": "Google",
        "Date": "11/2",
        "Summary": "Received",
        "Status": "Awaiting"
    }
    # Add more email data as needed
]

dfs = []

# Iterate through email data and create a DataFrame for each company
for email_data in email_data_list:
    df = pd.DataFrame([email_data], columns=["Company", "Date", "Summary", "Status"])
    dfs.append(df)

# Concatenate the list of DataFrames into a single DataFrame
data = pd.concat(dfs, ignore_index=True)

# Display the resulting DataFrame in Streamlit
st.dataframe(data, hide_index=True, width=1000)