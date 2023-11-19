import streamlit as st
import pandas as pd
import plotly.express as px
from auth import *

def load_view():
    login = st.button('Login')
    email_data = []
    st.write(get_login_str(), unsafe_allow_html=True)
    if st.button("display user"):  
        display_user()

    if login:
        email_data = [
        {"Company": "Facebook","Position":"Filler", "Status": "Determination","Date": "11/19" },
        {"Company": "Amazon","Position":"Filler", "Status": "Determination","Date": "11/19" },
        {"Company": "Apple","Position":"Filler", "Status": "Awaiting","Date": "11/19" },
        {"Company": "Netflix","Position":"Filler", "Status": "Interview Scheduled","Date": "11/19" },
        {"Company": "Google","Position":"Filler",   "Status": "Awaiting","Date": "11/19" },
        {"Company": "Microsoft","Position":"Filler", "Status": "Offer Extended","Date": "11/19" },
        {"Company": "LinkedIn","Position":"Filler", "Status": "Application Rejected","Date": "11/19" },
        {"Company": "Twitter","Position":"Filler", "Status": "Interview Completed","Date": "11/19" },
        {"Company": "Uber","Position":"Filler", "Status": "Application Under Review","Date": "11/19" },
        {"Company": "Airbnb","Position":"Filler", "Status": "Interview Declined","Date": "11/19" },
        {"Company": "Salesforce","Position":"Filler", "Status": "Application Shortlisted","Date": "11/19" },
        {"Company": "IBM","Position":"Filler", "Status": "Application Withdrawn","Date": "11/19" },
        {"Company": "Intel","Position":"Filler", "Status": "Phone Interview Scheduled","Date": "11/19" },
        {"Company": "HP","Position":"Filler", "Status": "Application on Hold","Date": "11/19" },
        {"Company": "Dell","Position":"Filler", "Status": "Final Round Interview","Date": "11/19" },
        {"Company": "Cisco","Position":"Filler", "Status": "Application Pending","Date": "11/19" },
        {"Company": "Oracle","Position":"Filler", "Status": "Application Expired","Date": "11/19" },
        {"Company": "Adobe","Position":"Filler", "Status": "Offer Negotiation","Date": "11/19" },
        {"Company": "VMware","Position":"Filler", "Status": "Application Reviewed","Date": "11/19" },
    ]

    st.markdown("<h1 style='text-align: center;'>🐶 <span style='color: #3DD56D;'>Job</span> Sniffer</h1>", unsafe_allow_html=True)

    # App description
    st.markdown("<h3 style='text-align: center;'>Fetch Your Future with Job Sniffer 🐾</h3>", unsafe_allow_html=True)
    st.subheader('',divider="green")
    st.markdown("<div style='text-align: center;'>Sniffing out job opportunities in your emails and delivering them right to your inbox!</div>", unsafe_allow_html=True)
    st.markdown('')



     # Concatenate the list of DataFrames into a single DataFrame if email_data is not empty
    if email_data:
        data = pd.DataFrame(email_data)
        st.dataframe(data, hide_index=True, width=1000, height = (len(email_data) + 1) * 35 + 3
)
