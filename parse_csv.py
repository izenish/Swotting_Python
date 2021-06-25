import csv

html_output=""

names=[]

with open('biostats.csv','r') as data_file:
    csv_data=csv.reader(data_file)

    'we dont want headers or first line of bad data'
    next(csv_data) #first row of data removed
    # next(csv_data)



    # print(list(csv_data))
    for line in (list(csv_data)):
        # print(line[0])
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)