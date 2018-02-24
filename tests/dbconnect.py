import datetime
from dbconnect import DbConnect

filename = "filename.mp4"
crime_title = "Amazing video :)"
t1 = 27
t2 = 32

if __name__ == '__main__':
    connection = DbConnect()
    connection.clip(filename, crime_title, datetime.datetime.now(), t1, t2)
    connection.push_to_db()
