from constants import Databases, Staff, User
from utils import get_data
import csv

if __name__ == "__main__":
    attendance_data = get_data(Databases.STAFF, Staff.ATTENDANCE)
    staff_data = get_data(Databases.USER, User.USERS)

    name_map = {}
    for i in staff_data:
        if not i:
            continue

        email = i.get("email", None)
        
        if not email:
            continue

        if not email.endswith("@hackillinois.org"):
            continue

        name_map[i["userId"]] = i["name"]

    print(len(attendance_data))
    attendance_out = []
    ct = 0
    for i in attendance_data:
        id = i["_id"]
        attendance = len(i["attendance"])
        try:
            name = name_map[id]
            attendance_out.append([name, attendance, id])
        except Exception as e:
            ct += 1
            print("nonexistent userid", e)
        
    print(len(attendance_out))
    with open("staff_attendance.out", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(attendance_out)
        