import streamlit as st
import pandas as pd
import plotly.express as px
from auth import *
from . import data_view as dv
from google.cloud import firestore

def load_view():
    db = firestore.Client.from_service_account_json("jobsniffer-firestore-key.json")
    # login = st.button('Login')
    # email_data = []
    flag=False
    if st.button("Login"):
        st.write(get_login_str(), unsafe_allow_html=True)
        flag=True
    b=None
    if st.button("Update Chart"):  
        b=display_user()
        flag=True
    # st.write(b)
    if(b):
        n=len(b)
        # st.write("I AM IN LENGTH")
        for i in range(n):
            # st.write("THE CURRENT INDEX IS ",i)
            d=b[i]
            doc_ref = db.collection("user").document(d["position"])
            doc_ref.set({
            "company": d["company"],
            "status": d["status"]
            })
    # st.write("before panda")
    df=None
    df=dv.firestore_to_panda()
    # st.write("after panda")
    
    if not df.empty and flag:
        print(df)
        st.write(df)

    
    

    

    st.markdown("<h1 style='text-align: center;'>🐶 <span style='color: #3DD56D;'>Job</span> Sniffer</h1>", unsafe_allow_html=True)

    # App description
    st.markdown("<h3 style='text-align: center;'>Fetch Your Future with Job Sniffer 🐾</h3>", unsafe_allow_html=True)
    st.subheader('',divider="green")
    st.markdown("<div style='text-align: center;'>Sniffing out job opportunities in your emails and delivering them right to your inbox!</div>", unsafe_allow_html=True)
    st.markdown('')



    #  # Concatenate the list of DataFrames into a single DataFrame if email_data is not empty
    # if email_data:
    #     data = pd.DataFrame(email_data)
    #     st.dataframe(data, hide_index=True, width=1000, height = (len(email_data) + 1) * 35 + 3)