import csv


path = r"D:\PythonProject\iris.csv"

with open(path) as file:
    headers = file.readline().split(',')
    data = csv.DictReader(file, fieldnames=headers, delimiter=',')

    for row in data:
        print(row)

