import csv

with open(input("Enter file path : "),'r') as file:
    reader = csv.DictReader(file, delimiter=input("Enter delimiter : "), quotechar=input("Enter quotechar : "))

    for data in reader:
        print(data)
