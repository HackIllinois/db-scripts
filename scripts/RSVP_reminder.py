from constants import Databases, Registration, Admission, Attendee
from utils import get_data
import pandas as pd
from bson import ObjectId
import pytz

if __name__ == "__main__":
    registration_data = get_data(Databases.REGISTRATION, Registration.APPLICATIONS)
    df = pd.DataFrame.from_dict(registration_data)
    
    # Only submitted applications 
    df = df[df["hasSubmitted"] == True]

    # get PENDING ACCEPTED RSVP ====================================
    admission_data = get_data(Databases.ADMISSION, Admission.DECISION)
    df2 = pd.DataFrame.from_dict(admission_data)
    df2 = df2[df2["status"] == "ACCEPTED"]
    df2 = df2[df2["response"]  == "PENDING"]
    pro_user_ids = df2["userId"].tolist()
    
    merged_df = pd.merge(df, df2, on='userId')
    merged_df = merged_df["emailAddress"]
    
    print(merged_df.to_list())