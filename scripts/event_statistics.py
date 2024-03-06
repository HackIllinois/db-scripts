from constants import Databases, Event
from utils import get_data
import pandas as pd

if __name__ == "__main__":
  event_data = get_data(Databases.EVENT, Event.ATTENDANCE)
  df = pd.DataFrame.from_dict(event_data)

  event_data2 = get_data(Databases.EVENT, Event.EVENTS)
  df2 = pd.DataFrame.from_dict(event_data2)

  merged_df = pd.merge(df, df2, on="eventId")

  target_events = ["Official Check-in", "Friday Dinner", "Friday Midnight Snack", "Saturday Lunch", "Saturday Dinner", "Saturday Midnight Snack", "Sunday Brunch"]
  merged_df = merged_df[merged_df["name"].isin(target_events)]

  merged_df["num_attendees"] = merged_df["attendees"].apply(len)

  stats = merged_df[["name", "eventId", "num_attendees"]]

  print(stats)