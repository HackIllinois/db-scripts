from constants import Databases, Registration
from utils import get_data
import pandas as pd
from bson import ObjectId
import pytz

def convert_to_cst(object_id_str):
    object_id = ObjectId(object_id_str)
    timestamp = object_id.generation_time

    # Define the CST timezone
    cst = pytz.timezone('America/Chicago')

    # Convert the timestamp to CST
    timestamp_cst = timestamp.replace(tzinfo=pytz.UTC).astimezone(cst)

    # Format the timestamp to a readable date and time in CST
    formatted_time_cst = timestamp_cst.strftime("%Y-%m-%d %H:%M:%S %Z")
    
    return formatted_time_cst


if __name__ == "__main__":
    registration_data = get_data(Databases.REGISTRATION, Registration.APPLICATIONS)
    df = pd.DataFrame.from_dict(registration_data)
    
    # Filter rows where 'hasSubmitted' is True
    df = df[df["hasSubmitted"] == True]

    # Convert ObjectId to timestamp in CST
    df["timestamp"] = [convert_to_cst(str(ObjectId(i))) for i in df["_id"]]
    df = df[["timestamp"] + [col for col in df.columns if col != "timestamp"]]

    # Drop the '_id' column
    df = df.drop(labels=["_id"], axis=1)

    # Save the DataFrame to a CSV file
    df.to_csv("registration_apps.csv", index=False)

    # Change the params to get stats here 
    print(len(df[df["major"] == "Computer Science"]))

    # Get unfinished applications
    # df = df["emailAddress"]
    # df.to_csv("unfinished_apps.cvs",index=False)