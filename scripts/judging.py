from constants import Databases, User, Registration, Admission, Attendee, Event, Attendee
from utils import get_data
import pandas as pd

# Collect from Devpost -> GitHub -> public name ? public name : github user id 
teams = [
  ["Lasya","yamommmy"]
  # ["github44485522"]
]

teamsUserIds = []

if __name__ == "__main__":
  # github name to userId
  user_data = get_data(Databases.USER, User.USERS)
  user_df = pd.DataFrame.from_dict(user_data)

  for team in teams: 
    tmp = []
    for member in team: 
      try:
        matching_row = user_df[user_df['name'] == member].values[0].tolist()
        targetUserId = matching_row[1]
        tmp.append(targetUserId)
      except:
        print("Name not found:", member)
        print()
    teamsUserIds.append(tmp)

  # userId to email 
  regis_data = get_data(Databases.REGISTRATION, Registration.APPLICATIONS)
  regis_df = pd.DataFrame.from_dict(regis_data)

  # userId to RSVP 
  admis_data = get_data(Databases.ADMISSION, Admission.DECISION)
  admis_df = pd.DataFrame.from_dict(admis_data)

  # userId to discord 
  profile_data = get_data(Databases.ATTENDEE, Attendee.PROFILE)
  profile_df = pd.DataFrame.from_dict(profile_data)

  # userId to check-in 
  event_data = get_data(Databases.EVENT, Event.ATTENDANCE)
  event_df = pd.DataFrame.from_dict(event_data)

  # Join all dfs 
  merged_df = pd.merge(regis_df, admis_df, on='userId', how='left')
  merged_df = pd.merge(merged_df, profile_df, on='userId', how='left')

  # print(merged_df.columns.values)

  final = []

  for team in teamsUserIds:
    for member in team: 

      # put this value in the spot for checkedIn: 
      print((event_df[event_df["eventId"] == "ca7927242bcf76b9ee8c5e210a587a98"]["attendees"].tolist()))
      try:
        new_row = {
          "userId": member,
          "emailAddress": merged_df[merged_df["userId"] == member].values[0].tolist()[6],
          "admittedPro": merged_df[merged_df["userId"] == member].values[0].tolist()[24],
          "response":merged_df[merged_df["userId"] == member].values[0].tolist()[27],
          "discordTag":merged_df[merged_df["userId"] == member].values[0].tolist()[32],
          # "checkedIn":
          # LAST PART NOT WORKING!!! 
          # JUST CHECK WITH EVENT_DF 
        }
        final.append(new_row)
      except:
        print("failed for:",member)
        print()
  
  print(final)

