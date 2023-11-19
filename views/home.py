import streamlit as st
import pandas as pd
import plotly.express as px


def load_view():
    login = st.button('Login')
    email_data = []
    if login:
        email_data = [
        {"Company": "Facebook", "Date": "07/30", "Summary": "Negative", "Status": "Determination"},
        {"Company": "Amazon", "Date": "09/23", "Summary": "Negative", "Status": "Determination"},
        {"Company": "Apple", "Date": "09/04", "Summary": "Positive", "Status": "Awaiting"},
        {"Company": "Netflix", "Date": "10/14", "Summary": "Positive", "Status": "Interview Scheduled"},
        {"Company": "Google", "Date": "11/02", "Summary": "Neutral", "Status": "Awaiting"},
        {"Company": "Microsoft", "Date": "01/15", "Summary": "Positive", "Status": "Offer Extended"},
        {"Company": "LinkedIn", "Date": "02/08", "Summary": "Negative", "Status": "Application Rejected"},
        {"Company": "Twitter", "Date": "03/22", "Summary": "Positive", "Status": "Interview Completed"},
        {"Company": "Uber", "Date": "04/05", "Summary": "Neutral", "Status": "Application Under Review"},
        {"Company": "Airbnb", "Date": "05/18", "Summary": "Negative", "Status": "Interview Declined"},
        {"Company": "Salesforce", "Date": "06/30", "Summary": "Positive", "Status": "Application Shortlisted"},
        {"Company": "IBM", "Date": "07/15", "Summary": "Negative", "Status": "Application Withdrawn"},
        {"Company": "Intel", "Date": "08/12", "Summary": "Positive", "Status": "Phone Interview Scheduled"},
        {"Company": "HP", "Date": "09/28", "Summary": "Negative", "Status": "Application on Hold"},
        {"Company": "Dell", "Date": "10/10", "Summary": "Positive", "Status": "Final Round Interview"},
        {"Company": "Cisco", "Date": "11/25", "Summary": "Neutral", "Status": "Application Pending"},
        {"Company": "Oracle", "Date": "12/07", "Summary": "Negative", "Status": "Application Expired"},
        {"Company": "Adobe", "Date": "01/20", "Summary": "Positive", "Status": "Offer Negotiation"},
        {"Company": "VMware", "Date": "02/14", "Summary": "Neutral", "Status": "Application Reviewed"},
    ]

    st.markdown("<h1 style='text-align: center;'>🐶 <span style='color: #3DD56D;'>Job</span> Sniffer</h1>", unsafe_allow_html=True)

    # App description
    st.markdown("<h3 style='text-align: center;'>Fetch Your Future with Job Sniffer 🐾</h3>", unsafe_allow_html=True)
    st.subheader('',divider="green")
    st.markdown("<div style='text-align: center;'>Sniffing out job opportunities in your emails and delivering them right to your inbox!</div>", unsafe_allow_html=True)
    st.markdown('')




    # Create a DataFrame with all months
    all_months_df = pd.DataFrame({'Month': range(1, 13)})

    # Create a dictionary to store the count of occurrences of each month and sentiment
    month_sentiment_count = {
        month: {"Negative": 0, "Positive": 0, "Neutral": 0} for month in range(1, 13)
    }

    # Iterate through email data and update the count for each month and sentiment
    for i in email_data:
        df = pd.DataFrame([i], columns=["Company", "Date", "Summary", "Status"])

        # Extract the month and sentiment from the date and summary, respectively
        month = pd.to_datetime(df['Date'], format='%m/%d').dt.month
        sentiment = df['Summary']

        # Update the count for the corresponding month and sentiment
        month_sentiment_count[month.values[0]][sentiment.values[0]] += 1

    # Convert month_sentiment_count to a DataFrame for easier plotting
    month_sentiment_count_df = pd.DataFrame(
        [{"Month": month, "Negative": count["Negative"], "Positive": count["Positive"], "Neutral": count["Neutral"]}
         for month, count in month_sentiment_count.items()]
    )

    # Convert the count columns to integers
    month_sentiment_count_df[['Negative', 'Positive', 'Neutral']] = month_sentiment_count_df[['Negative', 'Positive', 'Neutral']].astype(int)

    # Merge all_months_df with month_sentiment_count_df to ensure all months are included
    merged_df = pd.merge(all_months_df, month_sentiment_count_df, on='Month', how='left').fillna(0)

    # Concatenate the list of DataFrames into a single DataFrame if email_data is not empty
    if email_data:
        data = pd.concat([pd.DataFrame([i], columns=["Company", "Date", "Summary", "Status"]) for i in email_data], ignore_index=True)
        st.dataframe(data, hide_index=True, width=1000)
    
    # Horizontal Bar Graph Create a stacked bar chart with colors for sentiments
    fig = px.bar(
        merged_df,
        x='Month',
        y=['Negative', 'Positive', 'Neutral'],
        title='Sentiment Analysis by Month',
        labels={'value': 'Count', 'variable': 'Sentiment'},
        color_discrete_map={'Negative': 'red', 'Positive': 'green', 'Neutral': 'gray'},
        barmode='stack'

    #Verticle Bar Graph
    #  fig = px.bar(
    #     merged_df,
    #     x=['Negative', 'Positive', 'Neutral'],
    #     y="Month",
    #     title='Sentiment Analysis by Month',
    #     labels={'value': 'Count', 'variable': 'Sentiment'},
    #     color_discrete_map={'Negative': 'red', 'Positive': 'green', 'Neutral': 'gray'},
    #     barmode='stack',
    #     orientation='h'
    # )
    )

    # Set the y-axis tickmode and dtick to display only integer values
    fig.update_yaxes(tickmode='linear', dtick=1)

    # Set the x-axis tickmode and tickvals to display every x-axis value
    fig.update_xaxes(tickmode='array', tickvals=list(range(1, 13)))

    # Disable user scroll on the chart
    fig.update_layout(
        xaxis=dict(fixedrange=True),
        yaxis=dict(fixedrange=True),
        dragmode=False
    )
    if email_data:
        st.plotly_chart(fig)

