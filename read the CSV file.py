import csv
import datetime

def getage(now, dob):
    years = now.year - dob.year
    months = now.month - dob.month
    if now.day < dob.day:
        months -= 1
        while months < 0:
            months += 12
            years -= 1
    return '%syears %smonths'% (years, months)

with open(input("Enter file path : "),'r') as file:
    reader = csv.DictReader(file, delimiter=input("Enter delimiter : "), quotechar=input("Enter quotechar : "))

    for data in reader:
        today = datetime.date.today()
        DOB = datetime.datetime.strptime(data["birthdate"], "%Y-%m-%d").date()
        print(data)
        print("Age = " + getage(today, DOB) + "\n")