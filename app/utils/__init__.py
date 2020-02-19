import csv

def read (filename):
    headers=[]
    data=[]
    i=0
    j=0

    with open(filename, 'r') as csvfile:
        csv_reader=csv.reader(csvfile)
    for rows in csv_reader:
        if rows[1] is None:
            i+=1
        else:
            i+=1
            headers = rows
            break



    for rows in csv_reader:
        if (i==j):
            if rows is not None:
                data.append(rows)
        else:
            j+=1

    for entry in range(0, len(headers)):
        for element in range(entry, len(headers)):
            if (headers[entry]==headers[element]):
                print("Error:" + headers[element] + "is a duplicate header")
                return False

    for entry in data:
        for element in range(0, len(data[1])):
            if (entry[element]=='Y' or entry[element]=='y'):
                entry[element]="Yes"
            elif (entry[element]=='N' or entry[element]=='n'):
                entry[element]="No"
            elif (entry[element]==' '):
                entry[element]=None

    return [headers, data]