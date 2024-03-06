from constants import Databases, Registration, Admission, Attendee
from utils import get_data
import pandas as pd

if __name__ == "__main__":
    admission_data = get_data(Databases.ADMISSION, Admission.DECISION)
    df = pd.DataFrame.from_dict(admission_data)
    df = df.drop(labels=["_id","emailSent","admittedPro"], axis=1)

    registration_data = get_data(Databases.REGISTRATION, Registration.APPLICATIONS)
    df2 = pd.DataFrame.from_dict(registration_data)

    df2 = df2.drop(labels=["_id","hasSubmitted","isProApplicant","preferredName","gender","race",
                         "requestedTravelReimbursement","hackInterest","hackOutreach","dietaryRestrictions",
                         "hackEssay1","hackEssay2","optionalEssay","proEssay","considerForGeneral",
                         "degree","major","minor","gradYear"], axis=1)

    merged_df = pd.merge(df, df2, on='userId')
    merged_df.to_csv("reiumburseData.csv",index=False)
