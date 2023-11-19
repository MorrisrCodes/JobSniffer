import streamlit as st
from google.cloud import firestore

def load_view():
    test=st.button("PRESS HERE")
    if test:
        st.write("magic time")
        # Authenticate to Firestore with the JSON account key.
        db = firestore.Client.from_service_account_json("jobsniffer-firestore-key.json")
        users_ref = db.collection("user")

        for doc in users_ref.stream():
            #get fields
            job_position = doc.id
            company = doc.to_dict().get("Company", "")
            status = doc.to_dict().get("Status", "")

            # do the do with the data you gotta do
            st.write("Company: ", company, " / Job Position: ", job_position, " / Status: ", status)