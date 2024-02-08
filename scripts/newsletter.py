from constants import Databases, Registration, Newsletter
from utils import get_data
import pandas as pd
from bson import ObjectId
import pytz

'''
This script returns emails of prospective attendees that signed up through the newsletter and haven't already registered.
'''

if __name__ == "__main__":
  registration_data = get_data(Databases.REGISTRATION, Registration.APPLICATIONS)
  df_regis = pd.DataFrame.from_dict(registration_data)

  # Extract all email addresses
  registered_emails = df_regis['emailAddress'].tolist()

  # print(registered_emails)

  newsletter_data = get_data(Databases.NEWSLETTER, Newsletter.SUBSCRIPTIONS)

  # Get subscribers for desired newsletterIds
  subscribers = next(item['subscribers'] for item in newsletter_data if item['newsletterId'] == '2024_attendee_interest')
  subscribers += next(item['subscribers'] for item in newsletter_data if item['newsletterId'] == 'hackillinois2024_interest')

  # Get emails in subscribers not already registered
  print(list(set(subscribers).difference(registered_emails)))
    