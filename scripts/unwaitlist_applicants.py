from constants import Databases, Registration, Admission, Attendee
from utils import get_data
import pandas as pd
import requests, time

# API endpoint URLs for GET and POST requests
get_url = "https://adonix.hackillinois.org/admission/rsvp"
put_url = "https://adonix.hackillinois.org/admission/update"

# Headers for the requests (modify as needed)
headers = {
    "Authorization": "", # include token from adonix
    "Content-Type": "application/json"
}

# Function to make GET request
def make_get_request(user_id):
    response = requests.get(f"{get_url}/{user_id}", headers=headers)
    return response.json()

# Function to make POST request
def make_put_request(body):
    response = requests.put(put_url, json=body, headers=headers)
    return response.json()


if __name__ == "__main__":
    # get all WAITLISTED userIds ====================================
    admission_data = get_data(Databases.ADMISSION, Admission.DECISION)
    df2 = pd.DataFrame.from_dict(admission_data)
    df2 = df2[df2["status"] == "WAITLISTED"]
    waitlisted_user_ids = df2["userId"].tolist()

    print(len(waitlisted_user_ids))
    
    # get waitlisted statuses 
    mass_TBD_playload = [] 
    mass_admit_playload = []
    for id in waitlisted_user_ids:
        person1 = {
          "userId": id,
          "admittedPro": False,
          "emailSent": False,
          "reimbursementValue": 0,
          "response": "PENDING",
          "status": "TBD"
        }
        mass_TBD_playload.append(person1)

        person2 = {
          "userId": id,
          "admittedPro": False,
          "emailSent": False,
          "reimbursementValue": 0,
          "response": "PENDING",
          "status": "ACCEPTED"
        }
        mass_admit_playload.append(person2)
    
    print(mass_TBD_playload)

    # switch to TBD to trigger emails 
    # make_put_request(mass_TBD_playload[:30])
    # make_put_request(mass_TBD_playload[30:60])
    # make_put_request(mass_TBD_playload[60:])
    
    # # switch to ACCEPTED 
    # make_put_request(mass_admit_playload[:30])
    # make_put_request(mass_admit_playload[30:60])
    # make_put_request(mass_admit_playload[60:])

    print(len(waitlisted_user_ids))
    print(len(mass_admit_playload))
