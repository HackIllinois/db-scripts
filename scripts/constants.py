from enum import Enum

LATEST_BACKUP_DATE = "2024-02-22"

class Databases(Enum):
    ADMISSION = "admission"
    ATTENDEE = "attendee"
    AUTH = "auth"
    DECISION = "decision"
    EVENT = "event"
    MAIL = "mail"
    MENTOR = "mentor"
    NEWSLETTER = "newsletter"
    NOTIFICATIONS = "notifications"
    REGISTRATION = "registration"
    SHOP = "shop"
    STAFF = "staff"
    UPLOAD = "upload"
    USER = "user"

class Admission(Enum):
    DECISION = "decision"

class Attendee(Enum):
    FOLLOWING = "following"
    METADATA = "metadata"
    PROFILE = "profile"

class Auth(Enum):
    INFO = "info"

class Decision(Enum):
    INFO = "info"

class Event(Enum):
    ATTENDANCE = "attendance"
    EVENTS = "events"
    FOLLOWERS = "followers"
    METADATA = "metadata"
    PUBLICEVENTS = "publicevents"
    STAFFATTENDANCE = "staffattendance"
    STAFFEVENTS = "staffevents"

class Mail(Enum):
    LISTS = "lists"

class Mentor(Enum):
    OFFICEHOURS = "officehours"

class Newsletter(Enum):
    NEWSLETTERS = "newsletters"
    SUBSCRIPTIONS = "subscriptions"

class Notifications(Enum):
    NOTIFICATIONS = "notifications"
    ORDERS = "orders"
    TOPICS = "topics"
    USERS = "users"

class Puzzle(Enum):
    RUNESRIDDLES = "runesriddles"

class Registration(Enum):
    APPLICATIONS = "applications"

class Shop(Enum):
    ITEMS = "items"

class Staff(Enum):
    ATTENDANCE = "attendance"
    SHIFT = "shift"
    
class User(Enum):
    ATTENDANCE = "attendance"
    USERS = "users"