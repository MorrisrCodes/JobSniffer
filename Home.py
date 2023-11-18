import streamlit as st
import pandas as pd


# Streamlit layout settings
st.set_page_config(page_title="Home", layout="centered")

# Streamlit app layout for Home
st.title(":dog: :green[Job] Sniffer")

# App description
st.subheader(
    "Fetch Your Future with Job Sniffer 🐾",
    divider="green",
)
st.markdown(
    """Sniffing out job opportunities in your emails and delivering them right to your inbox!"""
)

# Check if the button has been clicked
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# Display the button only if it hasn't been clicked
if not st.session_state.button_clicked:
    clicked = st.button('Login', key='login_button')
    if clicked:
        st.session_state.button_clicked = True

# Streamlit app layout for App
if st.session_state.button_clicked:
    email_data = [
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
    ]

    st.title("Job Sniffer - App")

    data = []

    # Iterate through email data and create a DataFrame for each company
    for i in email_data:
        df = pd.DataFrame([i], columns=["Company", "Date", "Summary", "Status"])
        data.append(df)

    # Concatenate the list of DataFrames into a single DataFrame
    data = pd.concat(data, ignore_index=True)

    st.dataframe(data, hide_index=True, width=1000)
