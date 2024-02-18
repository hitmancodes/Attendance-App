import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("D:/hitmancodes/Projects/Attendance App/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendance-app-799b3-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data= {
    "01":
    {
        "Name":"Anshu Singh",
        "Major":"CSE",
        "Starting_Year":2019,
        "Total_Attendance":0,
        "Standing":"Poor",
        "Year":"Final",
        "Last_attendance_time":"2024-01-12 08:00:00"

    },
     "02":
    {
        "Name":"Gaurav Sharma",
        "Major":"ECE",
        "Starting_Year":2020,
        "Total_Attendance":0,
        "Standing":"Good",
        "Year":"Final",
        "Last_attendance_time":"2024-01-12 08:00:00"

    },
     "04":
    {
        "Name":"Ankit Yadav",
        "Major":"ECE",
        "Starting_Year":2020,
        "Total_Attendance":0,
        "Standing":"Good",
        "Year":"Final",
        "Last_attendance_time":"2024-01-12 08:00:00"

    },
     "05":
    {
        "Name":"Rutwij Nandankar",
        "Major":"ECE",
        "Starting_Year":2020,
        "Total_Attendance":0,
        "Standing":"Good",
        "Year":"Final",
        "Last_attendance_time":"2024-01-12 08:00:00"

    }
     
}
for key,value in data.items():
    ref.child(key).set(value)

