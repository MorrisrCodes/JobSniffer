import streamlit as st
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore, auth
from auth import *
from google.oauth2 import id_token
from google.auth.transport import requests
# import streamlit.ReportThread as ReportThread
# from streamlit.server.Server import Server
import os.path
import email
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
from google.auth import credentials
import mock

# Handle OAuth2 callback route
AUTHORIZATION_CODE = "code"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"# "http://localhost:8501"
client_id = "323856597657-o1v0baasi5d7tgkprlkjk0ji4g6sccr3.apps.googleusercontent.com"
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']

# load_dotenv()
# client_id = os.environ["GOOGLE_CLIENT_ID"]
# client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
# redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]

# Function to get user information after Google sign-in
def google_sign_in(loggedIn):
    if not loggedIn:
        if st.button("Sign in with Google"):
            st.write("TEST1")
            loggedIn=True
            # Create a flow instance
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scopes=SCOPES
            )
            st.write("TEST2")
            # Run the OAuth 2.0 authorization flow
            credentials = flow.run_local_server(
                host='localhost',
                port=8501,
                authorization_prompt_message='Please visit this URL: {url}',
                success_message='The auth flow is complete; you may close this window.',
                open_browser=True
            )
            st.write("TEST3")
            # Build the Google API service with the obtained credentials
            service = build('oauth2', 'v2', credentials=credentials)
            st.write("TEST4")
            # Retrieve user information
            user_info = service.userinfo().get().execute()
            st.write("TEST5")
            # Print or use the user information as needed
            email = user_info.get('email', '')
            name = user_info.get('name', '')
            st.write("TEST6")
            # Display user information
            st.write(f"Email: {email}")
            st.write(f"Name: {name}")
            st.write("TEST")
    else:
        st.write("logged in")

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("jobsniffer-firestore-key.json")

# Function to create a new user
def create_user(email):
    # Authenticate the user with Google credentials
    user = auth.get_user_by_email(email)

    # Retrieve user information
    uid = user.uid
    display_name = user.display_name

    # Create a new document for the user in the "users" collection
    user_ref = db.collection('users').document(uid)

    # Create subcollections "Becky" and "Carl" if they don't exist
    for collection_name in ["Becky", "Carl"]:
        collection_ref = user_ref.collection(collection_name).document()

        # Add user details to subcollections
        collection_ref.set({
            'name': display_name,
            'email': email,
            # Add other user details as needed
        })

def get_user_email(token):
    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(token)

        # Get the user's email from the decoded token
        user_email = decoded_token.get('email')

        return user_email
    except auth.InvalidIdTokenError:
        # Handle invalid ID token
        print("Invalid ID token.")
        return None

loggedIn=False

# Now let's make a reference to ALL of the posts
users_ref = db.collection("users").document("jobs").collection("Becky")

# For a reference to a collection, we use .stream() instead of .get()
for doc in users_ref.stream():# Get job position name
        job_position = doc.id

        # Get sentiment field
        sentiment = doc.to_dict().get("sentiment", "")

        # Print or process the data as needed
        st.write("Job Position: ", job_position)
        st.write("Sentiment: ", sentiment)

# This time, we're creating a NEW job reference for new position
doc_ref = db.collection("users").document("jobs").collection("Becky").document("MBA Internships - Summer 2024")

# And then uploading some data to that reference
doc_ref.set({
	"sentiment": "apprehensive"
})

# # Now let's make a reference to ALL of the posts
# users_ref = db.collection("users")

# For a reference to a collection, we use .stream() instead of .get()
for doc in users_ref.stream():# Get job position name
        job_position = doc.id

        # Get sentiment field
        sentiment = doc.to_dict().get("sentiment", "")

        # Print or process the data as needed
        st.write("Job Position: ", job_position)
        st.write("Sentiment: ", sentiment)

# This time, we're deleting a job reference for position
doc_ref = db.collection("users").document("jobs").collection("Becky").document("MBA Internships - Summer 2024")

# And then uploading some data to that reference
doc_ref.delete()

# create_user(get_user_email());

# email='email@gmail.com'
# name='name'
# if st.button("Sign in with Google"):
#     # Redirect the user to the Google Sign-In page
#     auth_url = "https://accounts.google.com/o/oauth2/auth"
#     client_id = "323856597657-o1v0baasi5d7tgkprlkjk0ji4g6sccr3.apps.googleusercontent.com"  # Replace with your actual client ID
#     redirect_uri = "http://localhost:8501"  # Replace with your redirect URI
#     scope = "openid"  # Replace with the desired scopes
#     state = "state123"  # Replace with a unique state value
#     auth_endpoint = f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"
#     st.markdown(f'<a href="{auth_endpoint}">Click here to sign in with Google</a>', unsafe_allow_html=True)

#     # creds = mock.Mock(spec=credentials.Credentials)
#     flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secrets.json',
#     scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'])

#     flow.run_local_server(host='localhost',
#         port=8501, 
#         authorization_prompt_message='Please visit this URL: {url}', 
#         success_message='The auth flow is complete; you may close this window.',
#         open_browser=True)
#     credentials = flow.credentials

#     service = build('calendar', 'v3', credentials=credentials)

#     user_info_service = build('oauth2', 'v2', credentials=creds)
#     user_info = user_info_service.userinfo().list().execute()
#     st.write(user_info['email'])
#     print(user_info['email'])
#     st.write(user_info['name'])
#     st.write("test")
#     email=user_info['email']
#     name=user_info['name']
# st.write("test2")
# st.write(email+' '+name)

if google_sign_in(loggedIn):
     st.write("AFTER BUTTON")