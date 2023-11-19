import streamlit as st
from google.cloud import firestore
import pandas as pd

def load_view():
    test=st.button("PRESS HERE")
    if test:
        # # st.write("magic time")
        # # Authenticate to Firestore with the JSON account key.
        # db = firestore.Client.from_service_account_json("jobsniffer-firestore-key.json")
        # users_ref = db.collection("user")

        # # for doc in users_ref.stream():
        # #     #get fields
        # #     job_position = doc.id
        # #     company = doc.to_dict().get("Company", "")
        # #     status = doc.to_dict().get("Status", "")

        # #     # do the do with the data you gotta do
        # #     st.write("Company: ", company, " / Job Position: ", job_position, " / Status: ", status)

        # # column names
        # columns = ['Company', 'Job Position', 'Status']

        # # dataframe
        # df = pd.DataFrame(columns=columns)

        # # firestore into panda
        # big_array=()
        # for doc in users_ref.stream():
        #     #get fields
        #     job_position = doc.id
        #     company = doc.to_dict().get("Company", "")
        #     status = doc.to_dict().get("Status", "")
        #     array=(company, job_position, status)
        #     big_array=big_array+array
        # # do the do with the data you gotta do
        # df = pd.concat(pd.Series(big_array))

        db = firestore.Client.from_service_account_json("jobsniffer-firestore-key.json")
        users = list(db.collection(u'user').stream())

        users_dict = list(map(lambda x: {'Company': x.get('Company'), 'Job Position': x.id, 'Status': x.get('Status'), "Date": "11/19/2023"}, users)) # users_dict = list(map(lambda x: x.to_dict(), users))
        df = pd.DataFrame(users_dict)
        
        # table_props = [
        #     ('width','100vw')
        #     ]
        # #dict(selector='table',props=table_props),
        # styles = [
        #     dict(selector='table',props=table_props),
        # ]
        # st.markdown(df.style.set_table_styles(styles).to_html(),unsafe_allow_html=True)

        # output
        print(df)
        st.write(df)