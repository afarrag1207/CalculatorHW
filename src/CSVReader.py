import csv

filename = "UnitTestAddition.csv"
fields = []
rows = []

with open (filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)




