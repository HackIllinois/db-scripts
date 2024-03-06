from constants import Databases, Event
from utils import get_data
import pandas as pd

if __name__ == "__main__":
    event_data = get_data(Databases.EVENT, Event.ATTENDANCE)
    df = pd.DataFrame.from_dict(event_data)

    event_data2 = get_data(Databases.EVENT, Event.EVENTS)
    df2 = pd.DataFrame.from_dict(event_data2)

    merged_df = pd.merge(df, df2, on='eventId')

    allowed_event_types = ["MINIEVENT", "WORKSHOP", "SPEAKER"]
    merged_df = merged_df[merged_df["eventType"].isin(allowed_event_types)]

    merged_df['num_attendees'] = merged_df['attendees'].apply(len)

    # Group by 'eventId' and sum the number of attendees for each event
    event_attendees = merged_df.groupby('eventId')['num_attendees'].sum()

    # Sort the events by the number of attendees in descending order and get the top 5
    top_5_events = event_attendees.sort_values(ascending=False).head(10)

    print(top_5_events)