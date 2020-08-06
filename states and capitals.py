import csv
with open('states.csv')as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    for row in readcsv:
        print(row)
with open("states.csv") as csv_file:
    line = csv_file.readlines()
