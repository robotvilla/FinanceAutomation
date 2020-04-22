import csv



with open('statements.CSV') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        row = row[:-1]
        row.pop(0)
        row.pop(3)
        
        #remove trailing element if it is empty
        while not row[-1]:
            row.pop()

        print(row)