import csv

DATA = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan'},
    {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
    {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
]
FILENAME = path = r"D:\PythonProject\ZAD12.csv"

with open(FILENAME, 'w', encoding='utf-8') as file:
    fieldnames = set().union(*(d.keys() for d in DATA))
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writeheader()

    for row in DATA:
        writer.writerow(row)