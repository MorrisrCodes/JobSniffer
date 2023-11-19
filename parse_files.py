import os.path
import email
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import google.generativeai as palm
import os
import json
import ast


palm.configure(api_key='API_KEY')
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]




if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build("gmail", "v1", credentials=creds)
one_week_ago = (datetime.now() - timedelta(days=1)).strftime("%Y/%m/%d")
query = f'after:{one_week_ago} category:primary'



gg=service.users().messages().list(userId='me', q=query).execute().get('messages', [])

bodies = {}#[" "] * len(gg)
j=0
for i in range(len(gg)):
    try:

        message = service.users().messages().get(userId='me', id=gg[i]['id']).execute()
        parts = message['payload']['parts']
        for part in parts:
            if part['mimeType'] == 'text/plain':
                body_data = part['body']['data']
                question="Below I have attached the details of emails I received in my inbox. Go through the text and see if it is about job applications and not workshops or tutorials?If so find the job position, company, the status of the job application,classify the status either as accepted, rejected, interviewing, submitted ,online assessment scheduled or None. Pass the information as a python dictionary with the fields company, position and status. Make sure that the status is classified as either accepted, rejected, interviewing, submitted or online assessment scheduled. If it is not a job application, don't write anything."

                email_body = base64.urlsafe_b64decode(body_data.encode('UTF-8')).decode('UTF-8')
                prompt=question+":"+str(email_body)
                # print("p")
                response=palm.generate_text(prompt=prompt)
                # print("r")
                if( response.result==None):
                    continue
                    
                else:
                    print(response.result)
                    context=ast.literal_eval( response.result)
                    

                    no_list=[None,'NA','None','','N/A','n/a','na','Not Found','Unknown','not a job application','Not a job application']
                    if not context:
                        continue
                    if any(context["company"]==c for c in no_list):
                        continue

                    if any(context["position"]==c for c in no_list):
                        continue

                    if any(context["status"]==c for c in no_list):
                        continue

                    bodies[j]=context
                    j+=1
                # print(i)
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    
# 
### Final format, yet to be decided. So sneak peak of the dictionary outputs after parsing all the emails from your inbox.
print(str(bodies))
f = open("demofile3.txt", "a")
for item in bodies.items():
    # print(item)
    f.write(str(item[1])+"\n")
f.close()


