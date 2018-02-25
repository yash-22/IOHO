import datetime
from dbconnect import DbConnect

filename = "50thBirthday.mp4"
crime_title = "Amazing video :)"
t1 = 27
t2 = 32

if __name__ == '__main__':
    connection = DbConnect()
    connection.clip(filename, t1, t2)
    connection.push_to_db(crime_title)
