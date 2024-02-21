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
    # Only applications that requested TR 
    df = df[df["requestedTravelReimbursement"] == True]

    # get all knights discord tags ====================================
    admission_data = get_data(Databases.ADMISSION, Admission.DECISION)
    df2 = pd.DataFrame.from_dict(admission_data)
    df2 = df2[df2["status"] == "ACCEPTED"]
    df2 = df2[df2["admittedPro"]  == True]
    pro_user_ids = df2["userId"].tolist()

    profile_data = get_data(Databases.ATTENDEE, Attendee.PROFILE)
    df = pd.DataFrame.from_dict(profile_data)
    
    merged_df = pd.merge(df, df2, on='userId')
    merged_df = merged_df["discordTag"]
    merged_df.to_csv("knights_discord.csv", index=False)
